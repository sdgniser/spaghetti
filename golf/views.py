from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.utils.timezone import now
from django.views.generic import DetailView, ListView

from .helpers import langs
from .forms import *
from .models import *

class ProblemList(ListView):
    model = GolfProblem
    template_name = 'golf_prob_list.html'
    all_states = ['active', 'future', 'past']
    state = 'active'
    context_object_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_states'] = self.all_states
        context['state'] = self.state
        return context

class ActiveGolfProblemList(ProblemList):
    state = 'active'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['probs'] = self.model.objects.filter(start__lt = now(),
                           end__gt = now()).order_by('end')
        return context

class PastGolfProblemList(ProblemList):
    state = 'past'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['probs'] = self.model.objects.filter(end__lt \
                           = now()).order_by('end')
        return context

class FutureGolfProblemList(ProblemList):
    state = 'future'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['probs'] = self.model.objects.filter(start__gt \
                           = now()).order_by('start')
        return context


def problem_detail(request, pid):
    """
    Displays the problem. Provides a form to record the solution if a user is
    logged in. Accepts a UTF-8 encoded plaintext file as solution.
    """
    prob = GolfProblem.objects.get(id=pid)

    if prob.is_upcoming():
        raise Http404('Problem not out yet.')

    if request.method == 'POST':
        # Throws an error if a POST request is received for a problem that is
        # not active
        if not prob.is_active():
            messages.error(request, 'The problem you tried to submit a \
            solution for is not active at this time.')
            return HttpResponseRedirect(reverse('golf:home'))

        form = SolutionForm(request.POST, request.FILES)
        if form.is_valid():
            code = form.cleaned_data['code']

            codefile = code.read()
            try:
                char_count = len(codefile.decode('utf-8', 'strict'))

                # Creating the Solution object
                Solution.objects.create(prob=prob, user=request.user,
                        lang=form.cleaned_data['lang'], code=code,
                        char_count=char_count)
             
            # Throws a hissy fit if it doesn't like the uploaded file
            except UnicodeDecodeError:
                messages.error(request, 'The file you uploaded could not be\
                processed by the backend. It only accepts UTF-8 encoded\
                plaintext files.')
                return HttpResponseRedirect(reverse('golf:problem', 
                    args=(pid,)))

            # Everything went nicely!
            messages.success(request, 'Your solution has been recorded\
            successfully. It will appear in the leaderboard once it is\
            verified to be working by one of the moderators.')
            return HttpResponseRedirect(reverse('golf:home'))

    # Stuff to do for a GET request
    else:
        form = None
        repeat_submission = False
        # Display a submission form only if the user is authenticated and the
        # problem is active
        if request.user.is_authenticated and prob.is_active():
            form = SolutionForm()
            if GolfProblem.objects.filter(id=pid, solution__user=request.user):
                repeat_submission = True
                form = None

    return render(request, 'golf_prob_detail.html', {'p': prob, 's_form': form,
                    'repeat_submission': repeat_submission,})

def problem_leader_view(request, pid):
    """
    Returns a ranked list of solutions for the problem in question.
    ranked_solutions is used by the template to construct the leaderboard

    The solutions are ranked by character count (lowest first) and submission
    time (earliest first).

    """
    prob = GolfProblem.objects.get(id=pid)
    ranked_solutions = Solution.objects.filter(prob=prob,
            is_correct=True).order_by('char_count', 'sub_time')

    return render(request, 'prob_leader.html', {'prob': prob, 'solns':
        ranked_solutions})

def user_leader_view(request):
    """
    Returns a ranked list of all registered users by thier 'score'.
    For details about the calculation of score, see Solution::calc_score

    """
    users = get_user_model().objects.all().order_by('-score')
    return render(request, 'user_leader.html', {'users': users})

def rules_view(request):
    return render(request, 'rules.html', {'langs': langs})

def faq_view(request):
    return render(request, 'faq.html')

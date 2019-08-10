from django.utils.timezone import now
from django.views.generic import DetailView, ListView

from .models import *

class ProblemList(ListView):
    model = Problem
    template_name = 'prob_list.htm'
    all_states = ['active', 'future', 'past']
    state = 'active'
    context_object_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_states'] = self.all_states
        context['state'] = self.state
        return context

class ActiveProblemList(ProblemList):
    state = 'active'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['probs'] = self.model.objects.filter(start__lt = now(),
                end__gt = now())
        return context

class PastProblemList(ProblemList):
    state = 'past'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['probs'] = self.model.objects.filter(end__lt = now())
        return context

class FutureProblemList(ProblemList):
    state = 'future'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['probs'] = self.model.objects.filter(start__gt = now()) 
        return context

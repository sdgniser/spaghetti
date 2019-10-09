from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timezone import now

from dirtyfields import DirtyFieldsMixin

from statistics import mean, stdev
from math import tanh

from .helpers import gen_file_name, allowed_langs, incorrect_reason_options


class GolfProblem(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField(max_length=2000)
    base_score = models.IntegerField(default=10)
    start = models.DateTimeField(default=now)
    end = models.DateTimeField(default=now)

    def __str__(self):
        return self.title

    def is_active(self):
        return (self.start <= now() and now() <= self.end)

    def is_past(self):
        return self.end < now()

    def is_upcoming(self):
        return self.start > now()

    def leader(self):
        """
        Returns the user model that has a solution with the lowest character
        count of this problem. In case of a clash, the solution which was
        submitted earlier is preferred.

        """
        ranked_leaders = get_user_model().objects.filter(solution__prob=self,
                solution__is_correct=True).order_by('solution__char_count',
                        'solution__sub_time')
        if ranked_leaders:
            return ranked_leaders[0]


class Solution(DirtyFieldsMixin, models.Model):
    """
    The model and the fields should be self explanatory.

    DirtyFieldsMixin has been added to calculate score when is_correct changes
    from False to True.

    """
    prob = models.ForeignKey(GolfProblem, on_delete=models.CASCADE)
    lang = models.CharField(max_length=100, choices=allowed_langs, null=False)
    # gen_file_name generates a random string of 12 characters. "Security".
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    code = models.FileField(upload_to=gen_file_name)
    instructions = models.TextField(max_length=300, default='')
    char_count = models.IntegerField()
    sub_time = models.DateTimeField(default=now)
    is_correct = models.BooleanField(default=False)

    is_incorrect = models.BooleanField(default=False)
    incorrect_reason = models.CharField(max_length=300, null=True, blank=True,
            verbose_name = 'Solution has been marked incorrect because')

    assigned_score = models.IntegerField(default=0)

    def __str__(self):
        return str(self.prob) + ' by ' + str(self.user)

    def avg_char_count(self, prob):
        return Solution.objects.filter(prob=prob,
                is_correct=True).aggregate(Avg('char_count'))

    # To detect if the field was changed. Provided by DirtyFieldsMixin.
    FIELDS_TO_CHECK = ['is_correct']

    def calc_score(self, MULT=3):
        """
        Calculates a score multiplier based on the solutions already submitted.

        Roughly: when the submitted solution has character count much larger
        than the average character count, the calculated score is
        1*base_score. If the character count is much smaller than the average
        character count, the calculated score is MULT*base_score

        See code for details.
        
        """
        prob = GolfProblem.objects.get(id=self.prob.id)
        all_soln = Solution.objects.filter(is_correct=True, prob=prob)

        char_count = self.char_count
        char_count_array = []
    
        for s in all_soln:
            char_count_array += [s.char_count]
    
        from math import inf
        avg_char_count = inf
        sd_char_count = 0.01 # Aah! Magic constant! AAAAH!
        if len(char_count_array) > 1:
            avg_char_count = mean(char_count_array)
            sd_char_count = stdev(char_count_array)
    
        mult = (1 + ((MULT-1)/2) + ((MULT-1)/2) 
                 * tanh((avg_char_count - char_count) / sd_char_count))

        return round(prob.base_score * mult, 0)

    def save(self, *args, **kwargs):
        """
        Overriding save() to detect if is_correct was changed.

        Be careful while verifying solutions.

        """
        score = self.calc_score()
        dirty = self.is_dirty()
        super().save(*args, **kwargs)

        if self.is_correct and dirty:
            self.assigned_score = score
            self.save()

from django.contrib import admin
from .models import *


class SolutionAdmin(admin.ModelAdmin):
    model = Solution
    list_display = ('__str__', 'lang', 'char_count', 'sub_time', 'is_correct',
            'is_incorrect')

class GolfProblemAdmin(admin.ModelAdmin):
    model = GolfProblem
    list_display = ('__str__', 'base_score', 'start', 'end', 'is_active')

admin.site.register(Solution, SolutionAdmin)
admin.site.register(GolfProblem, GolfProblemAdmin)

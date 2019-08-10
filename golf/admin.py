from django.contrib import admin
from .models import *

admin.site.register([GolfProblem, Solution])

from django.db import models

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timezone import now

from dirtyfields import DirtyFieldsMixin

from statistics import mean, stdev
from math import tanh

class Problem(models.Model):
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

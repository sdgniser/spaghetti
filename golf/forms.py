from django import forms

from .models import Solution

class SolutionForm(forms.ModelForm):
    """
    Form to record the solution.
    Usually displayed on the corresponding problem's detail page
    """
    class Meta:
        model = Solution
        fields = ['lang', 'code']

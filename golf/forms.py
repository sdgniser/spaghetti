from django import forms

from .models import Solution

class SolutionForm(forms.ModelForm):
    """
    Form to record the solution.
    Usually displayed on the corresponding problem's detail page
    """
    instructions = forms.CharField(
            widget=forms.Textarea, label='Compilation/Execution Instructions')
    class Meta:
        model = Solution
        fields = ['lang', 'instructions', 'code']

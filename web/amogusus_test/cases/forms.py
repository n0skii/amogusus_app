from django import forms
from .models import Case


class NativeCaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = {
            "name",
            "case_hash",
        }

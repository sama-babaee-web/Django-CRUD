from django import forms
from crud2.models import Candidate



class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = "__all__"
        

from django import forms
from . models import Lead, Agent

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'



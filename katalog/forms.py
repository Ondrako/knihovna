import imp
from django import forms

class KnihaForm(forms.Form):
    jmeno = forms.CharField(max_length=200, label="Zadej jmeno knihy")
from django import forms
from .models import Kniha

#class KnihaForm(forms.Form):
#    jmeno = forms.CharField(max_length=200, label="Zadej jmeno knihy", error_messages={"required": "Tohle policko je povinne.","max_length": "Moc dlouhy text, povoleno je maximalne 20 znaku"})
#   autor = forms.CharField(max_length=200, label="Jmeno autora")
#    recenze = forms.CharField(max_length=2000, label="Recenze knihy", widget=forms.Textarea)

class KnihaForm(forms.ModelForm):
    class Meta:
        model = Kniha
        #fields = "__all__" nedoporucuje se
        fields = ["jmeno", "autor", "recenze"]
        labels = {
            "jmeno": "Zadej jmeno knihy:",
            "autor": "Zadej jmeno autora:",
            "recenze": "Napis neco o knize:"
            }
        error_messages = {
            "jmeno": {
                "required": "Tohle policko je povinne.",
                "max_length": "Moc dlouhy text, povoleno je maximalne 20 znaku"
            }
        }
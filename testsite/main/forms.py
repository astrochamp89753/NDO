from django import forms

class UstvariNovSeznam(forms.Form):
    name = forms.CharField(label="Ime", max_length=200)
    check = forms.BooleanField(required=False)
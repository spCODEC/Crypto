from django import forms

class EnterCode(forms.Form):
    code = forms.CharField(max_length=150)
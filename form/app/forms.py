from django import forms

class Userreg(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
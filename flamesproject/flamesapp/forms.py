from django import forms

class flames(forms.Form):
    your_name = forms.CharField(max_length=30)
    your_partner = forms.CharField(max_length=30)
from django import forms

class PartyForm(forms.Form):
	subject = forms.CharField(max_length=50)
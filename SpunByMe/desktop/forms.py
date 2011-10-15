from django import forms

class PartyForm(forms.Form):
	name = forms.CharField(max_length=50)
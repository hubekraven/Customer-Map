from django import forms

class DealerSelectForm(forms.Form):
	dealerSelection = forms.ChoiceField('Selectionez')
from django import forms

class addProductForm(forms.Form):
	number = forms.CharField(widget=forms.TextInput())
	description = forms.CharField(widget=forms.TextInput())
	
	def clean(self):
		return self.cleaned_data

from django import forms
from demo.apps.ventas.models import production

class addProductForm(forms.ModelForm):
	class Meta:
		model = production
		exclude = {'status',}

"""
class addProductForm(forms.Form):
	number = forms.CharField(widget=forms.TextInput())
	description = forms.CharField(widget=forms.TextInput())
	image		= forms.ImageField(required=False)
	price		= forms.DecimalField(required=True)
	stock		= forms.IntegerField(required=True)

	def clean(self):
		return self.cleaned_data
"""
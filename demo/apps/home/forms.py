from django import forms
from django.contrib.auth.models import User
class ContactForm(forms.Form):
	Email	= forms.EmailField(widget=forms.TextInput())
	Title	= forms.CharField(widget=forms.TextInput())
	Text	= forms.CharField(widget=forms.Textarea())

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))

class RegisterForm(forms.Form):
	username = forms.CharField(label="User Name", widget=forms.TextInput())
	email = forms.EmailField(label="E-mail", widget=forms.TextInput())
	password_one = forms.CharField(label="Password", widget=forms.PasswordInput(render_value=False))
	password_two = forms.CharField(label="Conform Password", widget=forms.PasswordInput(render_value=False))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Username already exist!')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email already registered for another user!')

	def clean_password_two(self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('Password does not match!')
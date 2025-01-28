from django import forms

class CustomLoginForm(forms.Form):
    email = forms.EmailField(label='Email address', max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
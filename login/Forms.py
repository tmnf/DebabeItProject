from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.PasswordInput()
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField()
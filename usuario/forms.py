from django import forms
from captcha.fields import CaptchaField


class LoginCaptcha(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    senha = forms.PasswordInput()
    captcha = CaptchaField()
    
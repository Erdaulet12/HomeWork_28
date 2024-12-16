from django import forms
from captcha.fields import CaptchaField


class CustomForm(forms.Form):
    name = forms.CharField(max_length=255, label="Имя")
    email = forms.EmailField(label="Электронная почта")
    message = forms.CharField(widget=forms.Textarea, label="Сообщение")
    captcha = CaptchaField(label="Введите капчу")

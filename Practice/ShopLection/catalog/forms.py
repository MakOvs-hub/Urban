from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.Form): #Форма обратной связи
    name = forms.CharField(max_length=100, label="Ваше имя")    #CharField: Поле для текстовых данных.
    email = forms.EmailField(label="Ваш Email") #EmailField: Поле для электронной почты (встроенная проверка на корректность).
    message = forms.CharField(widget=forms.Textarea, label="Сообщение") #widget=forms.Textarea: Позволяет отобразить большое текстовое поле.

class CustomContactForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100)
    email = forms.EmailField(label='Ваш email')
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@example.com'):
            raise ValidationError('Email должен заканчиваться на @example.com')
        return email

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100, label="Имя")
    email = forms.EmailField(label="Email")
    feedback = forms.CharField(widget=forms.Textarea, label="Ваш отзыв")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise forms.ValidationError("Email должен оканчиваться на @example.com.")
        return email
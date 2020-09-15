from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    # Here we dont use modelform bcz here is no model associate with
    username=forms.CharField(max_length=100,label="Username")
    password=forms.CharField(max_length=100,label=" Password ",widget=forms.PasswordInput)
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError("Wrong Username or Password!!")
            return super(LoginForm, self).clean()

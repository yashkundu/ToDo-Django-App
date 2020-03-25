from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=30)
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())

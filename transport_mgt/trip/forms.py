from django import forms
from .models import SignUp

class SignUpModelForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = SignUp
        fields = [
            "first_name",
            "last_name",
            "email",
            "contact",
            "house_name",
            "street",
            "post_code",
            "city"
        ]


class SignInForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = SignUp
        fields = [
            'email'
        ]


class GuestAccessForm(forms.ModelForm):
    class Meta:
        model = SignUp

        fields = [
            "first_name",
            "last_name",
            "contact",
            "house_name",
            "street",
            "post_code",
            "city"

        ]
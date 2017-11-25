from django import forms
from .models import SignUp
from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget

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

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not ".com" in email:
            raise forms.ValidationError("Please enter a valid .Edu or .Com email address.")
        return email


class SignInForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class GuestAccessForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    contact = forms.CharField(max_length=100)
    house_name = forms.CharField(max_length=100)
    street = forms.CharField(max_length=100)
    post_code = forms.CharField(max_length=10)
    city = forms.CharField(max_length=100)

# class CityForm(forms.ModelForm):
#     class Meta:
#         model = SignUp


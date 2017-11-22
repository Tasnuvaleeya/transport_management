from django.contrib import admin
from .models import SignUp
from .forms import SignUpModelForm, SignInForm

# Register your models here.


class SignUpModelAdmin(admin.ModelAdmin):
    form = SignUpModelForm
    # class Meta:
    #     model = SignUp


class SignInModelAdmin(admin.ModelAdmin):
    form = SignInForm


admin.site.register(SignUp, SignUpModelAdmin)
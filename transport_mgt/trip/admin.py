from django.contrib import admin
from .models import SignUp
from .forms import SignUpModelForm, SignInForm
from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget

# Register your models here.

class TripAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widgets": GooglePointFieldWidget}
    }
class SignUpModelAdmin(admin.ModelAdmin):
    form = SignUpModelForm
    class Meta:
        model = SignUp


class SignInModelAdmin(admin.ModelAdmin):
    form = SignInForm


admin.site.register(SignUp, SignUpModelAdmin)
from django.shortcuts import render
from .models import SignUp
from .forms import SignUpModelForm, SignInForm, GuestAccessForm
# Create your views here.
def home_view(request):
    form = SignUpModelForm()
    context = {
        "form": form
    }
    if form.is_valid():
        form.save()
    return render(request, 'trip/signup_form.html', context)


def signin_view(request):
    form_signin = SignInForm()
    context = {
        "form_signin": form_signin
    }
    return render(request,'trip/signin_form.html',context)

def guest_access_view(request):
    form_guest= GuestAccessForm()
    context = {
        "form_guest": form_guest
    }
    return render(request, 'trip/guest_access_form.html', context)

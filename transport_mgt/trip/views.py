from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import ListView
from .models import SignUp
from django.urls import reverse_lazy,reverse
from .forms import SignUpModelForm, SignInForm, GuestAccessForm
# Create your views here.
def home_view(request):
    form = SignUpModelForm(request.POST or None)
    message = "Save Complete!"
    if form.is_valid():
        # instance = form.save(commit=False)
        form.save()

    context = {
        "form": form,
        "message": message
    }

    return render(request, 'trip/signup_form.html', context, message)
    # return HttpResponseRedirect(reverse_lazy("trip:signup-view"))

def signin_view(request):
    form_signin = SignInForm()
    context = {
        "form_signin": form_signin
    }
    return render(request, 'trip/signin_form.html',context)




def guest_access_view(request):
    form_guest = GuestAccessForm(request.POST or None)
    context = {
        "form_guest": form_guest
    }
    return render(request, 'trip/guest_access_form.html', context)



def trip_view(request):
    return render(request, 'trip/trip_list.html', {})
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from user.forms import UserRegistratinForm


# Create your views here.
def register_user(request):
    if request.user.is_authenticated:
        return HttpResponseForbidden("You're already logged in")

    if request.method == "POST":
        form = UserRegistratinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        return render(request, template_name='registration.html', context={'register_form': form})
    else:
        form = UserRegistratinForm()
        return render(request, template_name='registration.html', context={'register_form':form})


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')

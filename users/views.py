from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import LoginForm


# Create your views here.
def Login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'users/login.html',context)
def register_view(request):
    form=UserCreationForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password1 = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")
        if password1==password2:
            user=form.save()
            login(request,user)
            return redirect('/')
    else:
        # for username Duplication
        form = UserCreationForm()

    return render(request,'users/register.html',{'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')
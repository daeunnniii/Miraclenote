from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
from django.views.decorators.clickjacking import xframe_options_exempt

def index(request):
    cur_user = request.user
    if cur_user.is_authenticated:
        return redirect('mynote:index')
    else:
        return render(request, 'common/home.html')

def manual(request):
    return render(request, 'common/manual.html')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('common:login')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

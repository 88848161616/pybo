from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
from django.http import HttpResponseNotAllowed

def signup(request):
    """
    회원가입

    """
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'common/signup.html', {'form': form})
    elif request.method == 'GET':
        form = UserForm()
        return render(request, 'common/signup.html', {'form': form})
    else:
        return HttpResponseNotAllowed(['POST', 'GET'])


from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from customer.forms import LoginForm, RegisterModelForm


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('customer')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_page(request):
    if request.method == 'GET   ':
        logout(request)
        return redirect('customers')
    return render(request, '')


def register_page(request):
    if request.method == 'POST':
        form = RegisterModelForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            login(request, user)
            return redirect('customers')
    else:
        form = RegisterModelForm()

    return render(request, '', {'form': form})
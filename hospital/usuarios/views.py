from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "usuarios/registro.html", {'form': form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        for msg in form.error_messages:
            messages.error(request, form.error_messages[msg])
        return render(request, 'usuarios/registro.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            messages.error(request, 'invalid user')
        messages.error(request, 'invalid user')
    form = AuthenticationForm()
    return render(request, "registro/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('login')

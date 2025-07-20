from django.contrib.auth import authenticate, login , logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.views.generic import  DetailView ,UpdateView
from .models import User
from django import forms

from cart.models import Cart

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect('home')  
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
  
            user.save()
            login(request, user)
            Cart.objects.create(user=user)

            messages.success(request, 'Account created successfully.')
            return redirect('home') 
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


    
def user_logout(request):
    if hasattr(request.user, 'auth_token'):
        request.user.auth_token.delete()
    logout(request)

    return redirect('home') 


class UserDetailView(DetailView):
    model = User
    template_name = 'accounts/profile.html'

class UserUpdateView(UpdateView):
    model = User

    fields = [
        "username",
        'first_name',
        'last_name',
        'phone',
        'email',
        'address',
        'age',
        'gender',
        'countery',
        'city',
        'postcode',
    ]
    
    template_name = 'accounts/user_form.html'  
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})
 
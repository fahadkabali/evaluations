from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm



# Create your views here.
#Home page
def index(request):
    return render(request, 'index.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('home')
            else:
                # Handle invalid login attempt (e.g., display error message)
                pass
        else:
            # Handle form validation errors (e.g., display form errors)
            pass
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
    
def user_logout(request):
    logout(request)
    return redirect('login')
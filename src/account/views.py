from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.forms import ValidationError

from .forms import UserRegistrationForm

@login_required
def dashboard(request):
    return render(request, 
                  'registration/dashboard.html', 
                  {'section': 'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # if form is valid we can create new user
            user: User = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password2'])
            user.save()
            login(request, user)
            return render(request,
                          'registration/register_done.html',
                          {'new_user': user})
        else:
            raise ValidationError(f'Form is not valid: {str(", ".join(user_form.errors))}')
    else:
        user_form = UserRegistrationForm()
        return render(request, 
                      'registration/register.html',
                      {'user_form': user_form})

from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    # I suppose ModelForm based on User has its own password field but we can override it
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password',
                                widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields= ['username', 'first_name', 'email']
    
    # write my own validations for fields (clean_<fieldname>())
    # this method will run by .is_valid()
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords must match.')
        return cd['password2'] # set this value for field
    
    
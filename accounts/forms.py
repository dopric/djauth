from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterUserForm(UserCreationForm):
    email = forms.CharField(min_length=5, max_length=120)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    email.widget.attrs['class'] = 'form-control'
    email.widget.attrs['placeholder'] = 'Enter your email'
    email.label = 'Email' 
    email.help_text= ''# '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

    def __init__ (self,  *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = 'User Name'
        self.fields['username'].help_text = ''# '<span class="form-text text-muted"><small>Required. </small></span>'

        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = 'Password'
        self.fields['password1'].help_text = ''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = 'Confirm password'
        self.fields['password2'].help_text = ''



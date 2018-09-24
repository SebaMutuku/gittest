from django import forms
from django.contrib.auth.models import User
class userLogin(forms.ModelForm):
    Username=forms.CharField(label="Username:",required=True)
    Password=forms.CharField(label="Password:",required=True)
    class Meta:
        model=User
        fields=(
            'Username',
            'Password'
        )
class userRegisteration(forms.ModelForm):
    Email=forms.EmailField(label="Enter Email:",required=True)
    Username=forms.CharField(label="Enter Username:",required=True)
    Othername=forms.CharField(label="Other name:",required=True)
    Password1=forms.CharField(label="Enter Password:",widget=forms.PasswordInput,required=True)
    Password2=forms.CharField(label="Confirm Password:",widget=forms.PasswordInput,required=True)

    class Meta:
        model=User
        fields=(
            'Username',
            'Othername',
            'Email',
            'Password1',
            'Password2'
        )
        def save(self,commit=True):
            user=super(userRegisteration,self)
            user.Othername=forms.cleaned_data['Othername']
            user.email=forms.cleaned_data['Email']
            user.Password1=forms.cleaned_data['Password1']
            user.Password2=forms.cleaned_data['Password2']
            if commit:
                user.save()
            return user

class ResetPass(forms.ModelForm):
    Email=forms.EmailField(label="Confirm Email",required=True)
    fields=(
            'Email'
        )
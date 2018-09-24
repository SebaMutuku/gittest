from django import forms
from django.contrib.auth.models import User

class userRegisteration(forms.ModelForm):
    Email=forms.EmailField(label="Enter Email",required=True)
    Username=forms.CharField(label="Enter Username",required=True)
    Othername=forms.CharField(label="Other name",required=True)
    Password1=forms.CharField(label="Enter Password",widget=forms.PasswordInput,required=True)
    Password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput,required=True)

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

            if commit:
                user.save()

            return user

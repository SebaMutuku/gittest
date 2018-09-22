from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class userRegisteration(UserCreationForm):
    Email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=(
            'username',
            'Firstname',
            'Last_name',
            'Email',
            'Password1',
            'Password2'
        )
        def save(self,commit=True):
            user=super(userRegisteration,self),save(commit=False)
            user.firstname=forms.cleaned_data['Firstname']
            user.Last_name=forms.cleaned_data['Last_name']
            user.email=forms.cleaned_data['Email']

            if commit:
                user.save()

            return user

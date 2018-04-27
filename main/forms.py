from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from main.models import Author_detail , write_up



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )



class login_form(forms.ModelForm):
    

    class Meta:
        model = User
        fields = ( "username", "password" )        



class author_detail_form(forms.Form):
    # file = forms.FileField()
    description = forms.CharField(max_length=300, required=False, help_text='Optional.')



# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()
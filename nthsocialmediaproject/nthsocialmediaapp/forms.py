from django import forms
from .models import Post,Comments
from django.contrib.auth.models import User

class PostCreateForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = (
             'title',
             'body'

        )
class PostEditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=(
            'title',
            'body'
        )

class CommentForm(forms.ModelForm):
    content=forms.CharField(label="",widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Text Here..','rows': 3,'cols':50}))
    class Meta:
        model= Comments
        fields=('content',)



class UserLoginForm(forms.Form):
    username=forms.CharField(label='Username')
    password=forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password'
            }
        )
    )
    confirm_password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Confirm Password'
            }
        )
    )
    class Meta:
        model=User
        fields=('first_name','last_name','email','username')

    def clean_confirm_password(self):
        password=self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise
            forms.ValidationError('Passwords Not matched')
        else:
            return confirm_password        

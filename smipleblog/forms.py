from django import forms
from models import *

class RegisterForm(forms.ModelForm):
	class Meta:
		model=User
		fields = ('username','password','repassword','email',)

class LoginForm(forms.ModelForm):
	class Meta:
		model=User
		fields = ('username','password',)


class PostForm(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = ('title','content','desc',)

class CommentForm(forms.ModelForm):
		
	class Meta:
		mdoel = Comment
		fields = ('content',)

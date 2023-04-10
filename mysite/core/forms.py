from django import forms
from pagedown.widgets import PagedownWidget
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
	publish = forms.DateField(widget=forms.SelectDateWidget)
	intro = forms.CharField(widget=PagedownWidget)
	body = forms.CharField(widget=PagedownWidget)
	class Meta:
		model = Post
		fields = [
			'image',
			'title', 
			'intro',
			'body',

		]

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('author', 'text',)
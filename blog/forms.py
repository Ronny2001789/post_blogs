from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter post title'}),
            'content': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Write your post content...', 'rows': 10}),
            'categories': forms.CheckboxSelectMultiple(),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Write your comment...', 'rows': 4}),
        }
        labels = {
            'content': 'Your Comment',
        }

from django import forms
from posts.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'description')
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:150px'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:100px'}),
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')

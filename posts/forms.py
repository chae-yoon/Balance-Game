from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title', 
            'select1_content', 
            'select2_content', 
            'select1_image', 
            'select2_image',
            )
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )
        widgets = {
            'content': forms.Textarea(attrs={'rows':'3',}),
        }
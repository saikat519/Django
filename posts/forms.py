from django.forms import ModelForm
from .models import Post_table

class PostForm(ModelForm):
    class Meta:
        model=Post_table
        fields = ['title', 'content','image']

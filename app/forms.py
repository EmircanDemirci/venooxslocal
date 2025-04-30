from django import forms
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = ['title', 'content']
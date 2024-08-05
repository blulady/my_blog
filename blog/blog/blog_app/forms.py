from django import forms

from .models import Post
from cloudinary.forms import CloudinaryFileField


class ContactForm(forms.Form):
    name = forms.CharField(max_length=250)
    email = forms.EmailField(max_length=250)
    phone = forms.CharField(max_length=11)
    subject = forms.CharField(max_length=250)
    message = forms.CharField(widget=forms.Textarea)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'content', 'slug', 'author', 'img', 'status']
        widgets = {
            'img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            "status": forms.Select(choices=Post.options, attrs={'class': 'form-control'}),
        }



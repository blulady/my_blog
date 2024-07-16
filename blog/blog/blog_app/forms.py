from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=250)
    email = forms.EmailField(max_length=250)
    phone = forms.CharField(max_length=11)
    message = forms.CharField(widget=forms.Textarea)

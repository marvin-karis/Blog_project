from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    Subject = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=150, required=True)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)

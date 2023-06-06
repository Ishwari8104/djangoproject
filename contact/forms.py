from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
    phone_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'style': 'background-color: white; color: black; font-family: geologica;'}))
    class_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'style': 'background-color: white; color: black; font-family: geologica;'}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'style': 'background-color: white; color: black; font-family: geologica;'}))

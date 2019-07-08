from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model=Contact
        fields = [
            "name","email",
            "number","message"]

        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control","placeholder":"Name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "number": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Number"}),
            "message": forms.TextInput(attrs={"class": "form-control", "placeholder": "Message"}),

        }
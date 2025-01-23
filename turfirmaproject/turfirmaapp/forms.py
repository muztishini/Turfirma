from django import forms
from .models import Customers


class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = "first_name", "last_name", "email", "phone"


class LoginForm(forms.Form):
    phone = forms.CharField(label="Номер телефона")
    
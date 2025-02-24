from django import forms
from .models import Customers


# класс формы регистрации клиента
class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = "first_name", "last_name", "email", "phone"


# класс формы логина клиента
class LoginForm(forms.Form):
    phone = forms.CharField(label="Номер телефона")

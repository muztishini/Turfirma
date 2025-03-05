from django import forms
from .models import Customers, Reviews


# класс формы регистрации клиента
class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = "first_name", "last_name", "email", "phone"


# класс формы логина клиента
class LoginForm(forms.Form):
    phone = forms.CharField(label="Номер телефона")


# класс формы добавления отзыва
class ReviewForm(forms.Form):
    user = forms.CharField(label="Имя", max_length=50, required=False)
    review = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 66, 'style': 'border-radius: 5px; padding: 10px; border: 1px solid #ccc;'}), label="Отзыв", max_length=255)

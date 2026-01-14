from django import forms
from django.forms.widgets import NumberInput
from .models import Customers, Reviews, Application


# класс формы регистрации клиента
class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = "first_name", "last_name", "email", "phone"


# класс формы логина клиента
class LoginForm(forms.Form):
    phone = forms.CharField(label="Номер телефона")


# класс формы добавления отзыва
class ReviewForm(forms.ModelForm):
    review_type = forms.ChoiceField(
        choices=(('tour', 'Отзыв о туре'), ('excursion', 'Отзыв об экскурсии')),
        widget=forms.RadioSelect(),
        label='Выбор отзыва'
    )
    class Meta:
        model = Reviews
        fields = ['user', 'photo', 'review_type', 'tour', 'excursion', 'star', 'review']
        widgets = {
            'user': forms.TextInput(attrs={
                'placeholder': 'Введите имя или оставьте пустым для Anonymous',
                'class': 'form-control'
            }),
            'review': forms.Textarea(attrs={
                'placeholder': 'Ваш отзыв...',
                'rows': 4,
                'class': 'form-control'
            }),
            'star': forms.NumberInput(attrs={
                'placeholder': 'Ваша оценка (от 1 до 5)',
                'min': 1,
                'max':5,
                'class': 'form-control'
            }),
            'tour': forms.Select(attrs={
                'id': 'tour-block',
                'class': 'form-control'
            }),
            'excursion': forms.Select(attrs={
                'id': 'excursion-block',
                'class': 'form-control'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].initial = 'Anonymous'
        self.fields['user'].required = False

    def clean_user(self):
        user = self.cleaned_data.get('user', '').strip()
        if not user:
            return 'Anonymous'
        return user


# класс формы оставления заявки
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = "name", "phone"


class DateForm(forms.Form):
    date = forms.DateField(label="Выберете дату тура",
                           widget=NumberInput(attrs={'type': 'date'}))

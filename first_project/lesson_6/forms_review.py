from django import forms
from durationwidget.widgets import TimeDurationWidget
from django.core.validators import RegexValidator


class ExampleForm(forms.Form):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Номер телефона должен быть в формате '+999999999'")
    profile_picture = forms.ImageField(label="Картинка:", required=False)
    email = forms.EmailField(label="Электронная почта", initial="admin@admin.com")
    text = forms.CharField(label="Описание", widget=forms.Textarea(attrs={"rows": 5, "cols": 20}))
    score = forms.ChoiceField(label="Оценка", choices=[(str(i), i) for i in range(1, 6)])
    reaction = forms.BooleanField(label="Вам понравился товар?",
                                  widget=forms.RadioSelect(choices=[(True, 'Да'), (False, 'Нет')]))
    phone_number = forms.CharField(validators=[phone_regex], max_length=17)
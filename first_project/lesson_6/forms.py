from django import forms
from durationwidget.widgets import TimeDurationWidget
from django.contrib.auth.models import User


class MyForm(forms.Form):
    widget_attrs = {'class': 'form-control', 'placeholder': 'Placeholder'}

    gender = forms.ChoiceField(label="Пол", required=False,
                               choices=[("0", "Другой"), ("1", "Мужчина"), ("2", "Женщина")],
                               widget=forms.Select(
                                   attrs={**widget_attrs, **{'id': 'fieldGender'}}))

    name = forms.CharField(label="Имя пользователя",
                           error_messages={'required': 'Введите свободное имя пользователя'},
                           widget=forms.widgets.TextInput(
                               attrs={**widget_attrs, **{'id': 'fieldName'}}))

    email = forms.EmailField(label="Электронная почта", initial="admin@admin.com",
                             error_messages={'required': 'Введите корректную электронную почту'},
                             widget=forms.widgets.EmailInput(
                                 attrs={**widget_attrs, **{'id': 'fieldEmail'}}))

    password = forms.CharField(label="Пароль", max_length=20, min_length=10,
                               widget=forms.widgets.PasswordInput(
                                   attrs={**widget_attrs, **{'id': 'fieldPassword'}}))

    profile_picture = forms.ImageField(label="Аватар:", required=False,
                                       widget=forms.widgets.FileInput(
                                           attrs={'id': 'fieldPicture',
                                                  'class': 'form-control  form-control-sm'}))

    additional_file = forms.FileField(label="Договор:", required=False,
                                      widget=forms.widgets.FileInput(
                                          attrs={'id': 'fieldDocument',
                                                 'class': 'form-control form-control-sm'}))

    agreement = forms.BooleanField(label="Я ознакомился(лась) с условиями.",
                                   widget=forms.widgets.CheckboxInput(
                                       attrs={'id': 'fieldAgreement', 'class': 'form-check-input'}))

    average_score = forms.FloatField(label="Средний балл", initial=56.1,
                                     widget=forms.widgets.NumberInput(
                                         attrs={**widget_attrs, **{'id': 'fieldScore'}}))

    birthday = forms.DateField(label="Дата рождения",
                               widget=forms.SelectDateWidget(
                                   attrs={'id': 'fieldBirthday', 'style': 'width: 32.8%;',
                                          'class': 'form-control d-inline'}))

    work_experience = forms.DurationField(label="Затраченное время:", required=False, help_text=False,
                                          widget=TimeDurationWidget(show_seconds=False, show_minutes=False,
                                                                    attrs={'id': 'fieldExperience',
                                                                           'class': 'form-control d-inline me-2',
                                                                           'style': 'width:32%;'}))



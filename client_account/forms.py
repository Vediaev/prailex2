from django import forms
from django.contrib.auth.models import User
from .models import NaturalPerson, Applications, LegalEntity, IndividualEntrepreneur





class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class NaturalPersonEditForm(forms.ModelForm):
    class Meta:
        model = NaturalPerson
        fields = ('first_name',
                  "last_name",
                  "patronymic",
                  'date_of_birth',
                  "city",
                  "street",
                  "home",
                  "flat",
                  'phone_number',
                  'passport_data_series',
                  'passport_data_number',
                  'place_of_passport_issuance',
                  'date_of_issue')


class ApplicationsEditForm(forms.ModelForm):

    class Meta:
        model = Applications
        fields = ('author',
                  'tag',
                  'area_of_law',
                  'application')
        widgets = {'author': forms.HiddenInput()}


class LegalEntityEditForm(forms.ModelForm):
    class Meta:
        model = LegalEntity
        fields = ('name_of_the_organization',
                  'firstname_general_manager',
                  'lastname_general_manager',
                  'patronymic_general_manager',
                  'main_state_registration_number',
                  'organizational_and_legal_form',
                  'taxpayer_identification_number',
                  'constituent_document',
                  'code_of_the_reason_for_registration',
                  'Date_of_approval_of_the_constituent_document',
                  'legal_address',
                  'actual_address',
                  'phone_number')


class IndividualEntrepreneurForm(forms.ModelForm):
    class Meta:
        model = IndividualEntrepreneur
        fields = ("first_name",
                  "last_name",
                  'patronymic',
                  'main_state_registration_number_individual_entrepreneur',
                  'taxpayer_identification_number',
                  'number_of_the_registration_certificate',
                  'Date_of_approval_of_the_registration_certificate',
                  'registration_address',
                  'phone_number')

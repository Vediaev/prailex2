from django import forms
from .models import Application


class ApplicationEditForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ('tag',
                  'area_of_law',
                  'application_text',
                  'territory_of_the_host_application')

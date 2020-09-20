from django.contrib import admin
from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['author',
                    'tag',
                    'area_of_law',
                    'status_of_application',
                    'time_of_application_creature']

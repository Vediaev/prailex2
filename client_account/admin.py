from django.contrib import admin
from .models import NaturalPerson, Applications, LegalEntity, IndividualEntrepreneur


@admin.register(NaturalPerson)
class NaturalPersonAdmin(admin.ModelAdmin):
    list_display = ['user',
                    "first_name",
                    "last_name",
                    'date_of_birth',
                    'photo']


@admin.register(Applications)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['author',
                    'tag',
                    'area_of_law',
                    'time_of_application_creature']


@admin.register(LegalEntity)
class LegalEntityAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'name_of_the_organization',
                    'firstname_general_manager',
                    'lastname_general_manager',
                    'Date_of_approval_of_the_constituent_document']


@admin.register(IndividualEntrepreneur)
class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    list_display = ['user',
                    "first_name",
                    "last_name",
                    'main_state_registration_number_individual_entrepreneur',
                    'registration_address',
                    'phone_number']

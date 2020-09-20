from django.contrib import admin
from lawyer_account.models import LawFirm, BranchLawFirm, IndividualEntrepreneurLawyer, MemberOfTheBarChamber
# Register your models here.


@admin.register(LawFirm)
class LawFirmAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'name_law_firm',
                    'firstname_general_manager',
                    'lastname_general_manager',
                    'date_of_approval_of_the_constituent_document']


@admin.register(IndividualEntrepreneurLawyer)
class IndividualEntrepreneurLawyerAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'first_name',
                    'last_name',
                    'Date_of_approval_of_the_registration_certificate',
                    'phone_number']


@admin.register(BranchLawFirm)
class BranchLawFirmAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'name_branch_law_firm',
                    'firstname_general_manager',
                    'lastname_general_manager',
                    'name_main_law_firm',
                    'date_of_the_power_of_attorney']


@admin.register(MemberOfTheBarChamber)
class MemberOfTheBarChamberAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'first_name',
                    'last_name',
                    'bar_chamber',
                    'date_of_issue_certificates']

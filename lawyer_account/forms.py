from django import forms
from lawyer_account.models import LawFirm, BranchLawFirm, IndividualEntrepreneurLawyer, MemberOfTheBarChamber


class LawFirmEditForm(forms.ModelForm):
    class Meta:
        model = LawFirm
        fields = ('name_law_firm',
                  'firstname_general_manager',
                  'lastname_general_manager',
                  'patronymic_general_manager',
                  'constituent_document',
                  'date_of_approval_of_the_constituent_document',
                  'organizational_and_legal_form',
                  'main_state_registration_number',
                  'taxpayer_identification_number',
                  'code_of_the_reason_for_registration',
                  'payment_account',
                  'servicing_bank',
                  'bank_identification_code',
                  'legal_address',
                  'actual_address',
                  'phone_number')


class BranchLawFirmEditForm(forms.ModelForm):
    class Meta:
        model = BranchLawFirm
        fields = ('name_branch_law_firm',
                  'name_main_law_firm',
                  'firstname_general_manager',
                  'lastname_general_manager',
                  'patronymic_general_manager',
                  'actual_address',
                  'servicing_bank',
                  'payment_account',
                  'taxpayer_identification_number',
                  'date_of_the_power_of_attorney',
                  'main_state_registration_number',
                  'code_of_the_reason_for_registration',
                  'bank_identification_code',
                  'phone_number')


class IndividualEntrepreneurLawyerEditForm(forms.ModelForm):
    class Meta:
        model = IndividualEntrepreneurLawyer
        fields = ('first_name',
                  'last_name',
                  'patronymic',
                  'address_of_registration_of_an_individual_entrepreneur',
                  'main_state_registration_number_individual_entrepreneur',
                  'taxpayer_identification_number',
                  'number_of_the_registration_certificate',
                  'Date_of_approval_of_the_registration_certificate',
                  'phone_number',
                  'bank_identification_code',
                  'availability_of_office_space',
                  'address_office_space',
                  'availability_of_employees',
                  'payment_account',
                  'servicing_bank')


class MemberOfTheBarChamberEditForm(forms.ModelForm):
    class Meta:
        model = MemberOfTheBarChamber
        fields = ('first_name',
                  'last_name',
                  'patronymic',
                  'bar_chamber',
                  'bar_association',
                  'name_of_the_bar_association',
                  'registration_number',
                  'certificates_number',
                  'date_of_issue_certificates',
                  'authority_that_issued_the_certificate',
                  'phone_number',
                  'payment_account',
                  'servicing_bank',
                  'bank_identification_code',
                  'availability_of_office_space',
                  'address')

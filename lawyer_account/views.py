from django.shortcuts import render, redirect
from .models import LawFirm, IndividualEntrepreneurLawyer, BranchLawFirm, MemberOfTheBarChamber
from .forms import LawFirmEditForm, BranchLawFirmEditForm, IndividualEntrepreneurLawyerEditForm, MemberOfTheBarChamberEditForm
from django.contrib.auth.decorators import login_required
from application.models import Application
from about_us.models import HelpModel


# Create your views here.
def create_law_firm_profile(request):
    if request.method == 'POST':
        HelpModel.objects.create(user=request.user, type_of_user='Юрист', type_of_profile='Юридическая фирма')
        LawFirm.objects.create(user=request.user)
        law_firm_form = LawFirmEditForm(
            instance=request.user.lawfirm,
            data=request.POST,
            files=request.FILES)
        if law_firm_form.is_valid():
            law_firm_form.save()
            return redirect('lawyer_dashboard')


def create_individual_entrepreneur_lawyer_profile(request):
    if request.method == 'POST':
        HelpModel.objects.create(user=request.user, type_of_user='Юрист', type_of_profile='Индивидуальный предприниматель')
        IndividualEntrepreneurLawyer.objects.create(user=request.user)
        individual_entrepreneur_lawyer_form = IndividualEntrepreneurLawyerEditForm(
            instance=request.user.individualentrepreneurlawyer,
            data=request.POST,
            files=request.FILES)
        if individual_entrepreneur_lawyer_form.is_valid():
            individual_entrepreneur_lawyer_form.save()
            return redirect('lawyer_dashboard')


def create_branch_law_firm_profile(request):
    if request.method == 'POST':
        HelpModel.objects.create(user=request.user, type_of_user='Юрист', type_of_profile='Филиал юридической компании')
        BranchLawFirm.objects.create(user=request.user)
        branch_law_firm_form = BranchLawFirmEditForm(
            instance=request.user.branchlawfirm,
            data=request.POST,
            files=request.FILES)
        if branch_law_firm_form.is_valid():
            branch_law_firm_form.save()
            return redirect('lawyer_dashboard')


def create_member_of_the_bar_chamber_profile(request):
    if request.method == 'POST':
        HelpModel.objects.create(user=request.user, type_of_user='Юрист', type_of_profile='Член адвокатской палаты')
        MemberOfTheBarChamber.objects.create(user=request.user)
        member_of_the_bar_chamber_form = MemberOfTheBarChamberEditForm(
            instance=request.user.memberofthebarchamber,
            data=request.POST,
            files=request.FILES)
        if member_of_the_bar_chamber_form.is_valid():
            member_of_the_bar_chamber_form.save()
            return redirect('lawyer_dashboard')


@login_required
def view_lawyer_dashboard(request):
    list_applications = Application.objects.all()
    constitutional_right = Application.objects.filter(area_of_law='Конституционное право')
    Administrative_law = Application.objects.filter(area_of_law='Административное право')
    Civil_right = Application.objects.filter(area_of_law='Гражданское право')
    Criminal_law = Application.objects.filter(area_of_law='Уголовное право')
    Civil_procedural_law = Application.objects.filter(area_of_law='Гражданское процессуальное право')
    Arbitration_procedure_law = Application.objects.filter(area_of_law='Арбитражное процессуальное право')
    Criminal_procedure_law = Application.objects.filter(area_of_law='Уголовно-процессуальное право')
    Criminal_Executive_law = Application.objects.filter(area_of_law='Уголовно-исполнительное право')
    Financial_law = Application.objects.filter(area_of_law='Финансовое право')
    Labour_law = Application.objects.filter(area_of_law='Трудовое право')
    Land_law = Application.objects.filter(area_of_law='Земельное право')
    select_list_applications = Application.objects.filter(contractor=request.user)
    template = 'templates/lawyer_account/lawyer_dashboard.html'
    context = {'constitutional_right': constitutional_right,
               'Administrative_law': Administrative_law,
               'Civil_right': Civil_right,
               'Criminal_law': Criminal_law,
               'Civil_procedural_law': Civil_procedural_law,
               'Arbitration_procedure_law': Arbitration_procedure_law,
               'Criminal_procedure_law': Criminal_procedure_law,
               'Criminal_Executive_law': Criminal_Executive_law,
               'Financial_law': Financial_law,
               'Labour_law': Labour_law,
               'Land_law': Land_law,
               'select_list_applications': select_list_applications,
               'list_applications': list_applications}
    return render(request,
                  template,
                  context)

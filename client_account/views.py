from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import \
    UserRegistrationForm, \
    UserEditForm, \
    NaturalPersonEditForm, \
    ApplicationsEditForm, \
    LegalEntityEditForm, \
    IndividualEntrepreneurForm
from .models import NaturalPerson, LegalEntity, IndividualEntrepreneur
from application.models import Application
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from about_us.models import HelpModel


@login_required
def edit(request):
    if request.method == 'POST':
        if request.user.helpmodel.type_of_profile == 'Физическое лицо':
            profile_form = NaturalPersonEditForm(instance=request.user.naturalperson,
                                                 data=request.POST,
                                                 files=request.FILES)
            if profile_form.is_valid():
                profile_form.save()
                return redirect('dashboard')
        elif request.user.helpmodel.type_of_profile == 'Юридическое лицо':
            profile_form = LegalEntityEditForm(instance=request.user.legalentity,
                                               data=request.POST,
                                               files=request.FILES)
            if profile_form.is_valid():
                profile_form.save()
                return redirect('dashboard')
        elif request.user.helpmodel.type_of_profile == 'Индивидуальный предприниматель':
            profile_form = IndividualEntrepreneurForm(instance=request.user.individualentrepreneur,
                                                      data=request.POST,
                                                      files=request.FILES)
            if profile_form.is_valid():
                profile_form.save()
                return redirect('dashboard')
    else:
        profile_form = NaturalPersonEditForm(instance=request.user.naturalperson)
    return render(request,
                  'templates/client_account/edit.html',
                  {'profile_form': profile_form})


@login_required
def dashboard(request):
        list_applications = Application.objects.filter(author=request.user)
        template = 'templates/client_account/dashboard.html'
        if request.user.helpmodel.type_of_profile == 'Физическое лицо':
            print('Физическое лицо')
            author = request.user.naturalperson.first_name + request.user.naturalperson.last_name
        elif request.user.helpmodel.type_of_profile == 'Юридическое лицо':
            author = request.user.legalentity.name_of_the_organization
        elif request.user.helpmodel.type_of_profile == 'Индивидуальный предприниматель':
            author = request.user.individualentrepreneur.first_name + request.user.individualentrepreneur.last_name
        context = {'list_applications': list_applications, 'filter_author': author}
        return render(request,
                      template,
                      context)


def create_natural_person_profile(request):
    if request.method == 'POST':
        HelpModel.objects.create(user=request.user, type_of_user='Клиент', type_of_profile='Физическое лицо')
        NaturalPerson.objects.create(user=request.user, is_natural_person_profile=True)
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = NaturalPersonEditForm(instance=request.user.naturalperson,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('dashboard')


def create_legal_entity_profile(request):
    if request.method == 'POST':
        HelpModel.objects.create(user=request.user, type_of_user='Клиент', type_of_profile='Юридическое лицо')
        LegalEntity.objects.create(user=request.user,
                                   is_legal_entity_profile=True)
        legal_entity_profile_form = LegalEntityEditForm(instance=request.user.legalentity,
                                                        data=request.POST,
                                                        files=request.FILES)
        if legal_entity_profile_form.is_valid():
            legal_entity_profile_form.save()
            return redirect('dashboard')


def create_individual_entrepreneur_profile(request):
    if request.method == 'POST':
        HelpModel.objects.create(user=request.user, type_of_user='Клиент', type_of_profile='Индивидуальный предприниматель')
        IndividualEntrepreneur.objects.create(user=request.user, is_natural_person_profile=True)
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        individual_entrepreneur_profile_form = IndividualEntrepreneurForm(instance=request.user.IndividualEntrepreneur,
                                                                          data=request.POST,
                                                                          files=request.FILES)
        if user_form.is_valid() and individual_entrepreneur_profile_form.is_valid():
            user_form.save()
            individual_entrepreneur_profile_form.save()
            return redirect('dashboard')


@login_required
def edit_application(request):
    if request.method == 'POST':
        applications_form = ApplicationsEditForm(data=request.POST)
        if applications_form.is_valid():
            response = applications_form.save(commit=False)
            response.author = request.user
            response.save()
        #return render(request, 'templates/client_account/edit_application.html', {'application_form': applications_form})
        return redirect('dashboard')
    else:
        applications_form = ApplicationsEditForm()
    return render(request, 'templates/client_account/edit_application.html', {'application_form': applications_form})


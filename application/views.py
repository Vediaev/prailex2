from django.contrib.auth.decorators import login_required
from .forms import ApplicationEditForm
from django.shortcuts import render, redirect
from .models import Application


@login_required
def edit_application(request):
    if request.method == 'POST':
        applications_form = ApplicationEditForm(data=request.POST)
        if applications_form.is_valid():
            response = applications_form.save(commit=False)
            response.author = request.user
            response.save()
        return redirect('dashboard')
    else:
        applications_form = ApplicationEditForm()
    return render(request, 'templates/client_account/edit_application.html', {'application_form': applications_form})


def change_status_applications(request):
    pass


def view_application_dashboard(request):
    if request.method == 'POST':
        applications_form = ApplicationEditForm(data=request.POST)
        if applications_form.is_valid():
            response = applications_form.save(commit=False)
            response.author = request.user
            response.save()
        return redirect('dashboard')
    else:
        applications_form = ApplicationEditForm()
        list_of_applications = Application.objects.filter(author=request.user)
        context = {'applications_form': applications_form, 'list_of_applications': list_of_applications}
        return render(request, 'templates/Application/application_dashboard.html', context)

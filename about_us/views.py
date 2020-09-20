from django.shortcuts import render


def view_about_us_page(request):
    return render(request, 'templates/main/about_us.html')

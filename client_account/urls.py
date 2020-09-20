from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from application.views import edit_application

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('edit/', views.edit, name='edit'),
    path('edit_application/', edit_application, name='edit_application'),
    path('create_natural_person_profile/', views.create_natural_person_profile, name='create_natural_person_profile'),
    path('create_legal_entity_profile/', views.create_legal_entity_profile, name='create_legal_entity_profile'),
    path('create_individual_entrepreneur_profile/', views.create_individual_entrepreneur_profile, name='create_individual_entrepreneur_profile')
]

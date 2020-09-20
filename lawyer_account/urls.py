from django.urls import path
from . import views


urlpatterns = [
    path('create_law_firm_profile/', views.create_law_firm_profile, name='create_law_firm_profile'),
    path('create_individual_entrepreneur_lawyer_profile/', views.create_individual_entrepreneur_lawyer_profile, name='create_individual_entrepreneur_lawyer_profile'),
    path('create_branch_law_firm_profile/', views.create_branch_law_firm_profile, name='create_branch_law_firm_profile'),
    path('create_member_of_the_bar_chamber_profile/', views.create_member_of_the_bar_chamber_profile, name='create_member_of_the_bar_chamber_profile'),
    path('lawyer_dashboard/', views.view_lawyer_dashboard, name='lawyer_dashboard')
]

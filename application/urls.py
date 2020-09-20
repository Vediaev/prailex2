from django.urls import path
from . import views


urlpatterns = [
    path('edit_application/', views.edit_application, name='edit_application'),
]

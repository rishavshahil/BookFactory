from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('edit/', views.profile_edit, name='profile-edit'),
    path('changepassword/', views.change_password, name='change-password'),
    path('settings/', views.profile_settings, name='profile-settings'),
]
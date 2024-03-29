from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration_api_view),
    path('login/', views.login_api_view),
    path('confirmation/', views.confirmation_api_view),
]

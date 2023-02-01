from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.SingUp.as_view(), name="registrar")
]

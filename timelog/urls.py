from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("employee/<int:pk>", views.employee, name="employee"),
]

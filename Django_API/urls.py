from django.urls import path

from Django_API import views

urlpatterns = [
    path('', views.getData),
]

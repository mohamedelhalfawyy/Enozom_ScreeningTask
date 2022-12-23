from django.urls import path

from Django_API import views

urlpatterns = [
    path('', views.getData),
    path('get-country/<str:countryCode>/', views.get_specific_country),
]

from django.urls import path

from Django_API import views

urlpatterns = [
    path('', views.CountryList.as_view()),
    path('get-country/<str:countryCode>/', views.get_specific_country),
]

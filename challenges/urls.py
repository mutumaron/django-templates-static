from django.urls import path
from . import views

urlpatterns = [
    path("",views.home_page,name="index"),
    path("challenges/<int:month>",views.monthly_challenge_by_number),
    path("challenges/<str:month>", views.monthly_challenge,name="month-challenge")
]

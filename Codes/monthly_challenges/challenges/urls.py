from django.urls import path
from . import views

# urlpatterns = [
#     path("january", views.january),    #First parameter is the path and the second is the corresponding function that will be triggered
#     path("february", views.february)
# ]

urlpatterns = [
    path("",views.index),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]
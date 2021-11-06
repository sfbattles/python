from django.urls import path 

from . import views 

# the concrete value should be a string and converted to a string
urlpatterns = [ 
    path("", views.index, name="home"),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name='month-challenge'),
]
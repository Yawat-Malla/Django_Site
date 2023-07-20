from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="main_home"),
    path('/membership/', views.membership, name="main_membership"),
    path('/resources', views.resources, name="main_resources"),
    path('/team', views.team, name="main_team"),
    path('/contact', views.contact, name="main_contact"),
    path('/events', views.event, name="main_events"),
]
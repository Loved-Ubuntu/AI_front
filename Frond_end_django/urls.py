from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('settings', views.settings),
    path('information', views.information)
]

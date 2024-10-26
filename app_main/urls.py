from django.urls import path

from . import views


urlpatterns = [
    path('', views.DevelopersView.as_view(), name='developers'),
]

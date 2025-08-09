from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('create', views.add, name='create'),  # Create a new link
    path('<str:pk>', views.shorten, name='shorten'),  # Shorten link
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='/'),
    path('menu', views.about, name='menu'),
    path('bar', views.create, name='bar'),
    path('sign_up', views.sign_up, name='sign_up')
]
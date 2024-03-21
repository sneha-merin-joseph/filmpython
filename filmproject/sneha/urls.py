from django.urls import path
from . import views
# app_name='sneha'
urlpatterns = [
    path('', views.homepage, name=""),
    path('register', views.register, name='register'),
    path('login', views.login, name='login')
]
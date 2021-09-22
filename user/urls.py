from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout')
]

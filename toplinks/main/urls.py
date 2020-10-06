from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('loggedin/', views.loginn, name='login'),
    path('logout/', views.userlogout, name='logout'),
]

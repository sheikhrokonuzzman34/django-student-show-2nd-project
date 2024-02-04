from django.urls import path
from .views import *

urlpatterns = [

    path('user_dashboard', user_dashboard, name='user_dashboard'),

    path('register', register, name='register'),
    path('profileupdate', profileupdate, name='profileupdate'),
    
    path('login', login_page, name='login'),
    path('logout/', logout_view, name='logout_view'),


]

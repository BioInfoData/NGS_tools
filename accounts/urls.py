from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns =  [
    path('singup/', views.singup_view, name='singup_form'),
    path('login/', views.login_view, name='login_form'),
    path('logout/',views.logout_view, name = 'logout')
]
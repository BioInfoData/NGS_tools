from django.urls import path
from . import views


app_name = 'articles'

urlpatterns =  [
    path('', views.articles_list, name = 'articles_list'),
    path('<slug:slug>/', views.articale_detail, name='detail')  # This MUST me last url
]
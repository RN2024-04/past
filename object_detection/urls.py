from django.urls import path
from . import views


urlpatterns=[
    path('',views.index2),
    path('login/', views.login),
    path('home/',views.index2),
    path('register/', views.register),

]
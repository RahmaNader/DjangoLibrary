from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
urlpatterns = [
    #path('',views.signup,name='signup'),
    #path('', views.register_request, name="register"),
    path('/register', views.register, name="register"),
    #path('', views.register, name='register' ),
]

from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('',views.signup,name='signup'),
]

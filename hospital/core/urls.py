from django.urls import path,include
from .views import *


urlpatterns = [
    path('signup/',signup_view,name='signup'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('doctor_detail/',doctor_detail,name='doctor_detail'),
     path('doctor_detail/<int:pk>/',doctor_detail,name='doctor_detail'),

]
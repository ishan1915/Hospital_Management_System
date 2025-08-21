from django.urls import path,include
from .views import *


urlpatterns = [
    path('signup/',signup_view,name='signup'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('doctor_detail/',doctor_detail,name='doctor_detail'),
     path('doctor_details/<int:pk>/',doctor_details,name='doctor_details'),
     path('patient_detail/',patient_detail,name='patient_detail'),
    path('patient_details/<int:pk>/',patient_details,name='patient_details'),

    path('appointment_detail/',appointment_detail,name='appointment_detail'),
        path('appointment_details/<int:pk>/',appointment_details,name='appointment_details'),


]
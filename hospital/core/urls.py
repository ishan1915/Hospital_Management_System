from django.urls import path,include
from .views import *


urlpatterns = [
    path('signup/',signup_view,name='signup'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),

  #admin-related urls

    path('doctor_detail/',doctor_detail,name='doctor_detail'),
    path('doctor_details/<int:pk>/',doctor_details,name='doctor_details'),

    path('patient_detail/',patient_detail,name='patient_detail'),
    path('patient_details/<int:pk>/',patient_details,name='patient_details'),

    path('appointment_detail/',appointment_detail,name='appointment_detail'),
    path('appointment_details/<int:pk>/',appointment_details,name='appointment_details'),




    path('medical_record/',medical_details,name='medical_record'),
    path('medical_records/<int:pk>/',medical_records,name='medical_records'),

#patient related urls
   path('book_appointment/',book_appointment,name='book_appointment'),
   path('appointment_list/',user_appointmentlist,name='appointment_list'),


   path('user_dashboard/',user_dashboard,name='user_dashboard'),


]
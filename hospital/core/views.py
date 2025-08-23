from django.shortcuts import render,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny]) 
def signup_view(request):
    serializer=SignupSerializer(data=request.data)
    if serializer.is_valid():
        user=serializer.save()
        serializer=UserSerializer(user)
        return Response({"message":"user created sucessfully","user":serializer.data},status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username=request.data.get('username')
    password=request.data.get('password')
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        serializer=UserSerializer(user)
        return Response({"msg":"login sucessfull","user":serializer.data},status=status.HTTP_200_OK)
    return Response({"error": "Invalid credentials"},status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({"msg":"logout sucesss"},status=status.HTTP_200_OK)


@api_view(['POST','GET'])
@permission_classes([IsAdminUser])
def doctor_detail(request):
    if request.method=='GET':
      doctors=Doctor.objects.all()
      serializer=DoctorSerializer(doctors,many=True)
      return Response(serializer.data)


    elif request.method=='POST':
        serializer=DoctorSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status)


@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAdminUser])
def doctor_details(request,pk):
    try:
        doctor=Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return Response({"msg":"Doctor does not exist"},status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
         serializer=DoctorSerializer(doctor)
         return Response(serializer.data)
    

    elif request.method=='PUT':
        serializer=DoctorSerializer(doctor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer=DoctorSerializer(doctor)
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        
    elif request.method=='DELETE':
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
   


@api_view(['GET','POST'])
@permission_classes([IsAdminUser])
def patient_detail(request):
    if request.method=='GET':
        patient=Patient.objects.all()
        seriaizer=PatientSerializer(patient,many=True)
        return Response(seriaizer.data)
    

    elif request.method=='POST':
        serializer=PatientSerializer(data=request.data)
        if serializer.is_valid():
            seriaizer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAdminUser])
def patient_details(request,pk):
    if request.method=='GET':
        patient=Patient.objects.get(pk=pk)
        serializer=PatientSerializer(patient)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    

    elif request.method=='PUT':
        patient=Patient.objects.get(pk=pk)
        serializer=PatientSerializer(patient,data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer=PatientSerializer(patient)
            return Response({"msg":"sucess","user":serializer.data},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method=='DELETE':
        patient=Patient.objects.get(pk=pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
        

    

@api_view(['POST','GET' ])
@permission_classes([IsAdminUser])
def appointment_detail(request):
    if request.method=='POST':
        serializer=AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='GET':
        appointment=Appointment.objects.all()
        serializer=AppointmentSerializer(appointment,many=True)
        return Response(serializer.data)
    




@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAdminUser])
def appointment_details(request,pk):
    if request.method=='GET':
        appointment=Appointment.objects.get(pk=pk)
        serializer=AppointmentSerializer(appointment)
        return Response(serializer.data,status=status.HTTP_200_OK)
 
    elif request.method=='PUT':
        appointment=Appointment.objects.get(pk=pk)
        serializer=AppointmentSerializer(appointment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method=='DELETE':
        appointment=Appointment.objects.get(pk=pk)
        appointment.delete()
        return Response({"message":"Appointment is deleted"})



@api_view(['GET','POST'])
@permission_classes([IsAdminUser])
def medical_details(request):
    if request.method=='GET':
        medical=MedicalRecord.objects.all()
        serializer=MedicalSerializer(medical,many=True)
        return Response(serializer.data,status=200)
    
    elif request.method=='POST':
        serializer=MedicalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAdminUser])
def medical_records(request,pk):
    if request.method=='GET':
        medical=MedicalRecord.objects.get(pk=pk)
        serializer=MedicalSerializer(medical)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method=='PUT':
        medical=MedicalRecord.objects.get(pk=pk)
        serializer=MedicalSerializer(medical,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method=='DELETE':
        medical=MedicalRecord.objects.get(pk=pk)
        medical.delete()
        return Response({"message":"deleted"})
    


@api_view(['POST'])
def book_appointment(request):
    patient=Patient.objects.get(user=request.user)
    data=request.data.copy()
    data['patient']=patient.id
    serializer=AppointmentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['GET'])
def user_appointmentlist(request):
    try:
        patient=Patient.objects.get(user=request.user)
    except Patient.DoesNotExist:
        return Response({"msg":"patient not exist"})
    appointment=Appointment.objects.filter(patient=patient).order_by('-date','-time')
    serializer=AppointmentSerializer(appointment,many=True)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_dashboard(request):
    user=request.user
    serializer=UserSerializer(user)
    patient=Patient.objects.get(user=request.user)
    appointment=Appointment.objects.filter(patient=patient).order_by('-date')
    appointment_serializer=AppointmentSerializer(appointment,many=True)

    return Response({"user":serializer.data, "appointment":appointment_serializer.data})




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def doctor_dashboard(request):
    user=request.user
    serializer=UserSerializer(user)
    doctor=Doctor.objects.get(user=request.user)
    appointment=Appointment.objects.filter(doctor=doctor).order_by('-date','-time')
    appointment_serializer=AppointmentSerializer(appointment,many=True)
    return Response({"user":serializer.data,"appointment":appointment_serializer.data})


#doctor will get details of his patient
@api_view(['GET'])
@permission_classes([IsAuthenticated])   
def doctor_patient_details(request):
    user = request.user

    try:
        doctor = Doctor.objects.get(user=user)
    except Doctor.DoesNotExist:
        return Response({"error": "Doctor not found"}, status=404)

    patients = Patient.objects.filter(appointment__doctor=doctor).distinct()   
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)


#patient will able to see his doctor details
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def patient_doctordetails(request):
    user=request.user
    patient=get_object_or_404(Patient,user=user)
    doctor=Doctor.objects.filter(appointment__patient=patient)
    serializer=DoctorSerializer(doctor,many=True)
    return Response(serializer.data)
    

#doctor will able to create medicalRecord
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def doctor_createMedicalReport(request):
    user=request.user
    doctor=Doctor.objects.get(user=user)
    data=request.data.copy()
    data['doctor']=doctor.id
    serializer=MedicalSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)



#patient will able to see his medicalrecord
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def patient_medicaldetails(request):
    patient=Patient.objects.get(user=request.user)
    medical_records=MedicalRecord.objects.filter(patient=patient).order_by('-created_at')
    serializer=MedicalSerializer(medical_records,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
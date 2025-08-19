from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
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
    return Response(serializer.errors ,status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({"msg":"logout sucesss"},status=status.HTTP_200_OK)


@api_view(['POST','GET'])
@permission_classes([AllowAny])
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
def doctor_detail(request,pk):
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

    
   



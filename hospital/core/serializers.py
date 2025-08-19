from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Doctor,Patient


class UserSerializer(serializers.ModelSerializer):
    class  Meta:

       model=User
       fields=["id","username","email"]

class SignupSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["username","email","password"]

        def create(self,validated_data):
            user=User.objects.create_user(
                username=validated_data["username"],
                email=validated_data["email"],
                password=validated_data["password"],
            )
            return user





class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields='__all__'



class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields='__all__'
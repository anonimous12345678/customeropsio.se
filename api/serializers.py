from typing_extensions import Required
from wsgiref.validate import validator
from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class Userserializer(serializers.ModelSerializer):
    email = serializers.EmailField(Required=True,
    validators=[UniqueValidator(queryset=User.objects.all())])
   
    password=serializers.CharField(write_only=True,required=True,validators=[validate_password])
    confirm_password=serializers.CharField(write_only=True,required=True)
   
    class Meta:
      model=User
      fields=["username","email","password","first_name","last_name","company_details","mob_no","confirm_password"]
      extra_kwargs={
                   'first_name': {'required': True}, 
                   'last_name': {'required': True}, 
                   'company_details': {'required': True},
                    'mob_no': {'required': True}, 
      }
      
      def validate(self,attrs):
        if attrs['password']!=attrs['confirm_password']:
            raise serializers.ValidationError({"password":"password fields didn't match."})
        return attrs
    
       
def create(self,validated_data):
    user=User.objects.create(
        username=self.validated_data['username'],
        email=self.validated_data['email'],
        first_name=self.validated_data['first_name'],
        last_name=self.validated_data['last_name'],
        company_details=self.validated_data['company_details'],
        mob_no=self.validated_data['mob_no'],
    )
    user.set_password(validated_data['password'])
    user.save()
    return user
    

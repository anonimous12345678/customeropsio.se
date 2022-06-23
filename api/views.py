from django.shortcuts import render
from .serializers import Userserializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your views here.
class register(APIView):
    def post(self,request,format=None):
        serializer=Userserializer(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']='registered'
            data['username']=account.username
            data['first_name']=account.first_name
            data['last_name']=account.last_name
            data['company_details']=account.company_details
            data['mob_no']=account.mob_no
            token,create=Token.objects.get_or_create(user=account)
            data['token']=token.key
        else:
            data=serializer.errors
        return Response(data)



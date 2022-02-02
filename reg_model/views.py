import imp
from django.shortcuts import render
from rest_framework.serializers import SerializerMetaclass
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from .cosmosdb import CosmosDB


class RegModel(APIView):
    auth_class = [authentication.TokenAuthentication]
    permission_class = [permissions.IsAuthenticated]

    def get(self,**kwargs):
        pass

    def post(self,request):
        return Response(f"{request.data}")


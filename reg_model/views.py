import imp
from django.shortcuts import render
from rest_framework.serializers import SerializerMetaclass
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from .cosmosdb import CosmosDB

collection = 'models'

class RegModel(APIView):
    # auth_class = [authentication.TokenAuthentication]
    # permission_class = [permissions.IsAuthenticated]
    def get(self,**kwargs):
        pass

    def post(self,request):
        
        data = request.data
        id = data['id']
        cdb = CosmosDB(collection)
        cdb.insert(data)
        return Response(f"{cdb.find_by_id(id)}")


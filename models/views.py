from rest_framework.serializers import SerializerMetaclass
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.parsers import FileUploadParser
from .cosmosdb import CosmosDB
from .blobdb import BlobDB

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

class GetModel(APIView):
    def get(self,**kwargs):
        pass

    def post(self,request):

        data = request.data
        id = data['id']
        cdb = CosmosDB(collection)
        result = cdb.find_by_id(id)
        return Response(f"{result}")

class SaveModelFile(APIView):
    # parser_classes = [FileUploadParser]

    def post(self,request):
        file = request.data['file']
        filename = file.name
        blobDB = BlobDB()
        re = blobDB.create(id='123123123123',file=file)
        print(re)
        print(re.items())
        return Response(f'{filename}upload completed\n{re.items()}')
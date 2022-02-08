from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os,pathlib
import random

# print(os.getenv('BLOB_CON_STR'))
# client = BlobServiceClient.from_connection_string(os.environ['BLOB_CON_STR'])

# container = client.get_container_client('containertest')
# # if container.exists == False:
# #     container.create_container(name='containertest')

# # blob = container.get_blob_client(blob='testtest.zip')

# print(os.getcwd())
# with open('sample.zip',"rb") as f:
#     result = container.upload_blob(data=f,name='test2.zip',overwrite=True)
#     if result.exists:
#         print('upload completed')

class BlobDB():
    def __init__(self,container):
        self.con_str = os.environ['BLOB_CON_STR']
        self.client = BlobServiceClient.from_connection_string(self.con_str)
        self.container_name = container
        self.container_client = self.client.get_container_client(self.container_name)

    def upload(self,file):
        pass

    def get(self):
        pass

    def remove(self):
        pass

    def update(self):
        pass
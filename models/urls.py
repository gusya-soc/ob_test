from django.urls import path
from .views import RegModel,GetModel,SaveModelFile

urlpatterns = [
    path('reg_model',RegModel.as_view(), name='RegModel'),
    path('get_model',GetModel.as_view(),name='GetModel'),
    path(r'save_model/(?P<filename>[^/]+'),SaveModelFile.as_view(),name='SaveModelFile')
]
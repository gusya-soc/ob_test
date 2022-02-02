from django.urls import path
from .views import RegModel

urlpatterns = [
    path('',RegModel.as_view(), name='RegModel'),
]
from django.urls import path, include
from .views import *

urlpatterns = [
    path('contractors/', ContractorsView.as_view()),
    path('contractor/<int:pk>/', ContractorsView.as_view()),
]
from django.urls import path, include
from .views import *

urlpatterns = [
#position
  path('positions/', PositionsView.as_view(), name='elections'),
  path('update-postion/<int:pk>/', PositionsView.as_view(), name='update-position'),
#elections
  path('elections', ElectionView.as_view(), name='elections'),
  path('update-election/<int:pk>/', ElectionView.as_view(), name='update-election'),
#nominations
  #path('elections', ElectionView.as_view(), name='elections'),
  #path('update-election/<int:pk>/', ElectionView.as_view(), name='update-election'),
]
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class PositionsView(APIView):
  permission_classes = [IsAuthenticated]
  def get(self, request):
    positions = Positions.objects.filter(is_deleted=False).order_by('-id')
    serializer = PositionsSerializers(positions, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    data = request.data
    serializer = PositionsSerializers(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk):
    try:
      position = Positions.objects.get(pk=pk, is_deleted=False)
    except Positions.DoesNotExist:
      return Response({'error': 'Position not found'}, status=status.HTTP_404_NOT_FOUND)
        
    data = request.data
    serializer = PositionsSerializers(position, data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class ElectionView(APIView):
  permission_classes = [IsAuthenticated]
  def get(self, request):
    elections = Elections.objects.filter(is_deleted=False).order_by('-id')
    serializer = ElectionsSerializers(elections, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    data = request.data
    serializer = ElectionsSerializers(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk):
    try:
      election = Elections.objects.get(pk=pk, is_deleted=False)
    except Positions.DoesNotExist:
      return Response({'error': 'Election not found'}, status=status.HTTP_404_NOT_FOUND)
        
    data = request.data
    serializer = ElectionsSerializers(election, data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
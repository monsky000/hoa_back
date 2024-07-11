from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class AmenityView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        amenities = Amenities.objects.filter(is_deleted=False).order_by('-id')
        serializer = AmenitiesSerializers(amenities, many=True)
        return Response(serializer.data)
      
    def post(self, request):
        data = request.data
        serializer = AmenitiesSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            amenity = Amenities.objects.get(pk=pk, is_deleted=False)
        except Amenities.DoesNotExist:
            return Response({'error': 'Amenity not found'}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        serializer = AmenitiesSerializers(amenity, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
class ReservationView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        reservations = Reservations.objects.filter(is_deleted=False).order_by('-id')
        serializer = ReservationsSerializers(reservations, many=True)
        return Response(serializer.data)
      
    def post(self, request):
        data = request.data
        serializer = ReservationsSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            reservation = Reservations.objects.get(pk=pk, is_deleted=False)
        except Reservations.DoesNotExist:
            return Response({'error': 'Amenity Reservations not found'}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        serializer = AmenitiesSerializers(reservation, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MaintenanceView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        maintenance = Maintenance.objects.filter(is_deleted=False).order_by('-id')
        serializer = MaintenanceSerializers(maintenance, many=True)
        return Response(serializer.data)
      
    def post(self, request):
        data = request.data
        serializer = MaintenanceSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            maintenance = Maintenance.objects.get(pk=pk, is_deleted=False)
        except Maintenance.DoesNotExist:
            return Response({'error': 'Maintenance schedule not found'}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        serializer = MaintenanceSerializers(maintenance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      

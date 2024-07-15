from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class ContractorsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        contactors = Contractors.objects.filter(is_deleted=False).order_by('-id')
        serializer = ContractorsSerializers(contactors, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = ContractorsSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            contactor = Contractors.objects.get(pk=pk, is_deleted=False)
        except Contractors.DoesNotExist:
            return Response({'error': 'Contactor not found'}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        serializer = ContractorsSerializers(contactor, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

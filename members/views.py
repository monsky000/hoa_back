from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class MemberRegistrationView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        members = MemReg.objects.filter(is_deleted=False).order_by('-id')
        serializer = MembersSerializer(members, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = MembersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def put(self, request, pk):
    #     try:
    #         branch = Branches.objects.get(pk=pk, deleted=False)
    #     except Branches.DoesNotExist:
    #         return Response({'error': 'Branch not found'}, status=status.HTTP_404_NOT_FOUND)
        
    #     data = request.data
    #     serializer = BranchesSerializer(branch, data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    
    def post(self, request, *args, **kwargs):
        serializer = AddMemberSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


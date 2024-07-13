from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class MemberRegistrationView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        registration_forms = MemReg.objects.all()
        serializer = MembersSerializer(registration_forms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MembersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from user.serializers import UserSerializer

class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"가입실패!"}, status=status.HTTP_400_BAD_REQUEST)
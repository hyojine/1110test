from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from user.serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"가입실패!"}, status=status.HTTP_400_BAD_REQUEST)

#### 원래 강의에서는 serializers.py에서 하는데 공식문서에는 views.py에서 해도 된다고 나와있대서 여기서 한번 해봄
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# 여기서 mytokenobtainpairserializer을 정의해줘서 아래 클래스에서 따로 임포트할 필요없음
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email
        token["token_message"]="sparta_time_attack"

        return token
####

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
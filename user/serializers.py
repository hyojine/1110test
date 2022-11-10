from rest_framework import serializers
from user.models import MyUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields='__all__'
    def create(self,validated_data):
        user=super().create(validated_data)
        password = user.password
        user.set_password(password) #해싱
        user.save() #db에 저장
        return user

# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Add custom claims
#         token['name'] = user.name
#         # ...

#         return token

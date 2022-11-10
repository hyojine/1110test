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
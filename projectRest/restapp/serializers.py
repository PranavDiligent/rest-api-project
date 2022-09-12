from rest_framework import serializers
from . models import Student
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


    

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('id','username','password')

        extra_kwargs = {'password':{
            'write_only':True,
            'required':True
        }}

    def create(self,validated_data):
        # del validated_data['confirm_password']
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
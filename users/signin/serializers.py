from users.models import User 
from rest_framework import serializers
from django.contrib.auth import authenticate

class SigninSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise serializers.ValidationError("Senha incorreta.")
        else:
            raise serializers.ValidationError("Email e senha são obrigatórios.")

        return data



from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'password_2', 'address', 'is_staff']
    
    def validate(self, data):
        if data['password'] != data['password_2']:
            raise serializers.ValidationError("As senhas não são correspondentes.")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user

''' 
Remoção do campo password_2, necessário somente para confirmar a validação.

'''


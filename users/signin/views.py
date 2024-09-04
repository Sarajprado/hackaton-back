from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import SigninSerializer
from .serializers import authenticate

class LoginView(generics.GenericAPIView):
    serializer_class = SigninSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        email = data.get('email')

        user = authenticate(email=email, password=request.data.get('password'))
        if user:
            return Response({"error": "Credenciais inválidas."}, status=status.HTTP_400_BAD_REQUEST)





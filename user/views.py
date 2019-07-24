from django.contrib.auth import get_user_model, authenticate, login
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserLoginSerializer, UserRegistrationSerializer

User = get_user_model()


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):
        input_data = self.serializer_class(data=request.data)

        if input_data.is_valid():
            user = authenticate(**input_data.validated_data)

            if user:
                login(request, user)

            return Response({'message': 'Authorized'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Check your Login or Password'}, status=status.HTTP_406_NOT_ACCEPTABLE)


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        input_data = self.serializer_class(data=request.data)

        if input_data.is_valid():
            User.objects.create_user(**input_data.validated_data)

            return Response(status=status.HTTP_201_CREATED)

        return Response(input_data.errors, status=status.HTTP_401_UNAUTHORIZED)

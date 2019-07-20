from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    password = serializers.CharField(style={'placeholder': 'password', 'input_type': 'password'})

    class Meta:
        model = User
        fields = ('email', 'password')


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'group', 'balance')

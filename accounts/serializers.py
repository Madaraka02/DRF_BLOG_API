from rest_framework import serializers, validators
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

        extra_kwargs= {
            "password":{"write_only":True},
            "email":{
                "required":True,
                "validators":[
                    validators.UniqueValidator(
                        User.objects.all(), "A user with this email exists"
                    )
                ]
            }}

    def create(self, validated_data):
        username = validated_data.get("username")
        email = validated_data.get("email")
        password = validated_data.get("password")
        first_name = validated_data.get("first_name")
        last_name = validated_data.get("last_name")


        user = User.objects.create(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        return user

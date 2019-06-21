from django.contrib.auth import get_user_model
from rest_framework import serializers


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True)  # Why this is write only?

    # Do the registering in the serializer stage since it doens't have ta model to work with?
    def create(self, validated_data):
        user = UserModel.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = UserModel  # why this?
        fields = ('id', 'username', 'password') # what's the field for?
        
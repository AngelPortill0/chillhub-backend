from rest_framework.serializers import ModelSerializer

from auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("uuid", "username", "email", "first_name", "last_name", "groups")

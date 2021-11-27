from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)
    email = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile

        fields = [
            "id",
            "username",
            "hospital",
            "profession",
            "pin",
            "mobile",
            "email",
            "gender",
        ]
    

    def get_username(self, obj):
        return obj.name.username

    def get_email(self, obj):
        return obj.name.email
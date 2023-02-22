from rest_framework import serializers

from app01.models import UserInfo


class UserinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'

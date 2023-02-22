from rest_framework import serializers
from app01 import models


class UserModelSerializers(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    last_update = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = models.UserInfo
        fields = ['id', 'username', 'create_time', 'last_update', 'is_delete']

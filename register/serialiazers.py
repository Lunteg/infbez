from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'usr', 'pwd']
        extra_kwargs = {
            'pwd': {'write_only': True}
        }

    def create(self, validated_data):
        pwd = validated_data.pop('pwd', None)
        instance = self.Meta.model(**validated_data)
        if pwd is not None:
            instance.set_password(pwd)
        instance.save()
        return instance
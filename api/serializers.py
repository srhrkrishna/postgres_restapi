from rest_framework import serializers
from api.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True, allow_blank=False, max_length=100)
    lastname = serializers.CharField(required=True, allow_blank=False, max_length=100)
    
    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.save()
        return instance
    class Meta:
        model = User
        fields = ('id', 'username', 'lastname')
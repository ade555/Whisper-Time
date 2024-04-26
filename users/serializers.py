from rest_framework import serializers

from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
    
    def create(self, validated_data):
        user = super().create(validated_data)
        password = validated_data["password"]
        user.set_password(password)
        user.save()
        return user
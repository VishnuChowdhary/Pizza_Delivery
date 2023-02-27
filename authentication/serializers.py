from authentication.models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=80)
    phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
    password = serializers.CharField(min_length=8)
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']
        
    def validate(self, attrs):
        username_exists = User.objects.filter(username=attrs['username']).exists()
        if username_exists:
            raise serializers.ValidationError(detail="Use with Username already exists")
        email_exists = User.objects.filter(username=attrs['email']).exists()
        if email_exists:
            raise serializers.ValidationError(detail="User with Email already exists")
        phonenumber_exists = User.objects.filter(username=attrs['phone_number']).exists()
        if phonenumber_exists:
            raise serializers.ValidationError(detail="User with Phonenumber already exists")
        return super().validate(attrs)

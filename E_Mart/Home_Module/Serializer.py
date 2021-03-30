from rest_framework import serializers
from .models import User

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','username','is_social_user','is_active']
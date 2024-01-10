from rest_framework import serializers
from ..models.models import Chatterloopusers

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chatterloopusers
        fields = ['userID', 'isActivated', 'isVerified']
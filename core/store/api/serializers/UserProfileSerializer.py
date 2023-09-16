from rest_framework import serializers
from store.models import UserProfile
from rest_framework.fields import CurrentUserDefault

class UserProfileSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=CurrentUserDefault())
    
    class Meta:
        model = UserProfile
        fields = '__all__'
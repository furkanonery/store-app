from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from store.models import UserProfile
from store.api.serializers import UserProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserProfileViewSet(APIView):

    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication]

    def get(self, request, format=None):
        user = UserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

    def patch(self, request, format=None):
        user_profile = UserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(user_profile, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
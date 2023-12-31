from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.core.cache import cache
from rest_framework import generics
from django.contrib.auth.models import User
from user.serializers import RegisterSerializer

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        token = cache.get(user.pk)
        if token:
            return Response({
                'token': token,
                'user_id': user.pk
            })
        else:
            token, created = Token.objects.get_or_create(user=user)
            cache.set(user.pk, token.key)
            return Response({
                'token': token.key,
                'user_id': user.pk
            })
    
class LogoutView(ObtainAuthToken):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        cache.delete(user.pk)
        Token.objects.filter(user=user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
from rest_framework.viewsets import GenericViewSet
from store.models import Cart
from store.api.serializers import CartSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from store.api.permissions import OwnYourCartsOrOrder
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response

class CartViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):

    permission_classes = [IsAuthenticated, OwnYourCartsOrOrder]
    authentication_classes = [TokenAuthentication,]

    def get_queryset(self):

        queryset = Cart.objects.filter(user = self.request.user)
        return queryset
    
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if self.request.user.id == request.data['user']:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            headers = self.get_success_headers(serializer.data)
            return Response({"Detail": "Authentication credentials were not provided."}, status=status.HTTP_403_FORBIDDEN, headers=headers)
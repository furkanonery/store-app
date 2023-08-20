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
        
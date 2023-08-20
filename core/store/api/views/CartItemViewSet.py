from rest_framework.viewsets import GenericViewSet
from store.models import CartItem, Cart
from store.api.serializers import CartItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from store.api.permissions import OwnYourCartsOrOrder
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

class CartItemViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,]
    queryset = CartItem.objects.all()

    def get_queryset(self):
        queryset = CartItem.objects.filter(cart__user=self.request.user)
        return queryset
    serializer_class = CartItemSerializer

    def perform_create(self, serializer):
        serializer.save(cart = Cart.objects.filter(user = self.request.user).last())
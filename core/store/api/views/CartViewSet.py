from rest_framework.viewsets import GenericViewSet
from store.models import Cart
from store.api.serializers import CartSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from store.api.permissions import OwnYourCartsOrOrder
from rest_framework import mixins

class CartViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):

    permission_classes = [IsAuthenticated, OwnYourCartsOrOrder]
    authentication_classes = [TokenAuthentication,]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
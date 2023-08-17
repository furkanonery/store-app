from rest_framework import viewsets
from store.models import Order
from store.api.serializers import OrderSerializer
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from store.api.permissions import OwnYourCartsOrOrder

class OrderViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet,
                   mixins.ListModelMixin
                   ):
    
    permission_classes = [IsAuthenticated, OwnYourCartsOrOrder]
    authentication_classes = [TokenAuthentication,]

    def get_queryset(self):

        queryset = Order.objects.filter(user = self.request.user)
        return queryset

    serializer_class = OrderSerializer
from rest_framework import viewsets
from store.models import Order, OrderItem, Cart, CartItem
from store.api.serializers import OrderSerializer
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from store.api.permissions import OwnYourCartsOrOrder
from rest_framework import status
from rest_framework.response import Response
from decimal import Decimal

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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        response = OrderSerializer(Order.objects.last())
        return Response(response.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):

        cart_items = CartItem.objects.filter(cart=Cart.objects.get(user=self.request.user))

        order = Order.objects.create(user=self.request.user)

        total_price = Decimal(0.00)

        for item in cart_items:
            OrderItem.objects.create(order = order, product = item.product, quantity = item.quantity)
            total_price += item.quantity * item.product.price

        order.total_price = total_price
        order.save()

        

from rest_framework import serializers
from store.models import Order, OrderItem
from store.api.serializers import ProductSerializer
from rest_framework.fields import CurrentUserDefault

class OrderItemSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = OrderItem
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(source="orderitem_set", many=True, read_only=True)
    products = ProductSerializer(many=True, read_only=True)
    user = serializers.HiddenField(default=CurrentUserDefault())
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = '__all__'
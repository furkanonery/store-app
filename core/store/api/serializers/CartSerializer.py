from rest_framework import serializers
from store.models import Cart, CartItem
from store.api.serializers import ProductSerializer
from rest_framework.fields import CurrentUserDefault

class CartItemSerializer(serializers.ModelSerializer):
    cart = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = CartItem
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(source="cartitem_set", many=True, read_only=True)
    products = ProductSerializer(many=True, read_only=True)
    user = serializers.HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Cart
        fields = "__all__"

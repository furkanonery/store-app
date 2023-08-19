from rest_framework import serializers
from store.models import Cart, CartItem
from store.api.serializers import ProductSerializer

class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):

    cart_items = CartItemSerializer(source='cartitem_set', many=True)
    user = serializers.StringRelatedField()
    products = serializers.PrimaryKeyRelatedField(source='products.all', many=True, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'
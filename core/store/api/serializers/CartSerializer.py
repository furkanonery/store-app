from rest_framework import serializers
from store.models import Cart
from store.api.serializers import ProductSerializer

class CartSerializer(serializers.ModelSerializer):

    products = ProductSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Cart
        fields = '__all__'
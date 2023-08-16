from rest_framework import serializers
from store.models import Product
class ProductSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = '__all__'

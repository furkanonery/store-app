from rest_framework import serializers
from store.models.Product import Product

class ProductSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['description','name','id']

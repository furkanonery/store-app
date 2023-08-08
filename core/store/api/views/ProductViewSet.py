from rest_framework import viewsets
from store.models import Product
from store.api.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated

class ProductViewSet(viewsets.ModelViewSet):

    permission_classes = []

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
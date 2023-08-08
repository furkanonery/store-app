from rest_framework import viewsets
from store.models import Product
from store.api.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class ProductViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
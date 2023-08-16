from rest_framework import viewsets
from store.models import Product
from store.api.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class ProductViewSet(viewsets.ModelViewSet):

    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,]
    serializer_class = ProductSerializer

    def get_queryset(self):
    
        category = self.request.query_params.get('category')

        if category:
            queryset = Product.objects.filter(category__name=category)
            return queryset
        queryset = Product.objects.all()
        return queryset

        
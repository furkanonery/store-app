from rest_framework.viewsets import GenericViewSet
from store.models import Category
from store.api.serializers import CategorySerializer
from rest_framework import mixins

class CategoryViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
        
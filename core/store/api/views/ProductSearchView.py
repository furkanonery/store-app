from rest_framework import generics
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from store.documents import ProductDocument
from store.api.serializers import ProductSearchSerializer

class ProductSearchViewSet(DocumentViewSet):
    document = ProductDocument
    serializer_class = ProductSearchSerializer

    filter_backends = [
        FilteringFilterBackend,
        SearchFilterBackend,
    ]

    search_fields = (
        'name',
        'description',
    )

    filter_fields = {
        'category': 'category__id',
    }
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from store.api.views import ProductViewSet, CartViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='Product')
router.register(r'carts', CartViewSet, basename='Cart')
router.register(r'orders', OrderViewSet, basename='Order')

urlpatterns = [
    path('', include(router.urls)),
]

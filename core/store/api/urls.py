from django.urls import path, include
from rest_framework.routers import DefaultRouter
from store.api.views import ProductViewSet, CartViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='Product')
router.register(r'carts', CartViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

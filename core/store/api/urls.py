from django.urls import path, include
from rest_framework.routers import DefaultRouter
from store.api.views import (ProductViewSet, 
                             CartViewSet, 
                             OrderViewSet, 
                             CartItemViewSet, 
                             CategoryViewSet, 
                             ProductSearchViewSet,
                             UserProfileViewSet,)

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='Product')
router.register(r'carts', CartViewSet, basename='Cart')
router.register(r'orders', OrderViewSet, basename='Order')
router.register(r'cartitems', CartItemViewSet, basename='CartItem')
router.register(r'categories', CategoryViewSet, basename='Category')
router.register(r'search', ProductSearchViewSet, basename='Search')

urlpatterns = [
    path('', include(router.urls)),
    path('userprofile/', UserProfileViewSet.as_view(), name='userprofile-update'),
]

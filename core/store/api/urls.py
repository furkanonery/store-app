from django.urls import path, include
from rest_framework.routers import DefaultRouter
from store.api.views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

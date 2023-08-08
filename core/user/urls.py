from django.urls import path
from user.views import UserLoginAPIView

urlpatterns = [
    path('', UserLoginAPIView.as_view(), name='login'),
]
from django.urls import path
from user.views import CustomAuthToken

urlpatterns = [
    path('login/', CustomAuthToken.as_view())
]
from django.urls import path
from user.views import CustomAuthToken, LogoutView

urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='custom-login'),
    path('logout/', LogoutView.as_view(), name='custom-logout')
]
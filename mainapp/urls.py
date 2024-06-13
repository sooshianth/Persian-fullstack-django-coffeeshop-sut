from django.urls import path
from .views import homepage, RegisterView


urlpatterns = [
    path('', homepage, name='index'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
]

from django.urls import path
from .views import homepage, LogInView, SignUpView

urlpatterns = [
    path('', homepage, name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
]

from django.urls import path
from .views import homepage, SignUpView

urlpatterns = [
    path('', homepage, name='index'),
    path('signup/', SignUpView.as_view, name='signup')
]

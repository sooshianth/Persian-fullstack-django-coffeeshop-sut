from django.urls import path
from . import views

urlpatterns = [    
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]

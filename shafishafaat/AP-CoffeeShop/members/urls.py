from django.urls import path
from . import views

urlpatterns = [    
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('forget_password/', views.password_reset_view, name='forget_password'),
]

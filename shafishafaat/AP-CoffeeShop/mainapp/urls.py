from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='index'),
    path('create_product/', views.ProductCreateView.as_view(), name='create_product'),
    path('store/', views.store_view, name='store'),
    path('management/', views.management_panel, name='management_panel'),
    path('select_storage/', views.select_storage_view, name='select_storage'),
    path('update_storage/<int:pk>',views.StorageUpdateView.as_view(),name='update_storage'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('finalize_order/', views.finalize_order, name='finalize_order'),
    path('order_history/', views.order_history, name='order_history'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_quantity/<int:product_id>/', views.update_quantity, name='update_quantity'),
]


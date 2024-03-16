
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)

from apps.views import RegisterCreateAPIView, ProductListView, CategoryListView, UserLoginAPIView, ProductDetailView
from root import settings

urlpatterns = [
    path('api/token/', TokenObtainSlidingView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh'),
    path('users/sign-up', RegisterCreateAPIView.as_view(), name='register'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('users/sign-in', UserLoginAPIView.as_view(), name='register'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]


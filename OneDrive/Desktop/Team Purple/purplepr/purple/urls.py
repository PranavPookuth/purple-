from django.urls import path
from . views import *

urlpatterns=[
    path('register/',RegisterView.as_view(),name='register'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
    path('request-otp/',RequestOTPView.as_view(),name='request-otp'),
    path('login/',LoginView.as_view(),name='login'),
    path('user/',UserListCreateView.as_view(),name='user-list'),
    path('user/<int:pk>/',UserDetailView.as_view(),name='user-details'),
    path('category/',CategoryCreateView.as_view(),name='category'),
    path('category/<int:pk>/',CategoryDetailView.as_view(),name='category-details'),
    path('products/',ProductListCreateView.as_view(),name='product-list'),
    path('products/<int:pk>',ProductDetailView.as_view(),name='product-details'),
    path('bannerimage/',BannerListCreateview.as_view(),name='banner-image'),
    path('bannerimage/<int:pk>/',BannerDetailView.as_view(),name='banner-details'),
    path('carousel/',CarouselListCreateView.as_view(),name='carousel-list'),
    path('carosuel/<int:pk>/',CarouselDetailView.as_view(),name='carousel-detail'),

]
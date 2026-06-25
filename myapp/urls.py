from django.contrib import admin
from django.urls import path, include
from .import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('inventory/', views.CreateInv.as_view(), name='createinv'),
    path('inventory/<int:pk>/', views.EditInv.as_view(), name='EditInv'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('inventory/reorder-list/',
         views. ReorderListView.as_view(), name='reorder-list'),
    path('inventory/<int:pk>/send-email/',
         views.SendOrderEmailView.as_view(), name='send-email'),

]

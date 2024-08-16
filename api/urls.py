from api import views
from django.urls import path


urlpatterns = [
    path('prodact_list/', views.ProdactList.as_view()),
    path('category_list/', views.CategoryList.as_view()),
    path('CategoryDetailSerializer/<int:pk>/', views.CategoryDetailSerializer.as_view()),
    path('ProductDetailSerializer/<int:pk>/', views.ProductDetailSerializer.as_view()),
    path('log_in/', views.log_in),
              ]
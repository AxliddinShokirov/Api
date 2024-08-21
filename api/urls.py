from api import views
from django.urls import path


urlpatterns = [
    path('prodact_list/', views.ProdactList.as_view()),
    path('category_list/', views.CategoryList.as_view()),
    path('CategoryDetailSerializer/<int:pk>/', views.CategoryDetailSerializer.as_view()),
    path('ProductDetailSerializer/<int:pk>/', views.ProductDetailSerializer.as_view()),
    path('log_in/', views.log_in),
    path(' CartDetailSerializer/<int:id>/', views.CartDetailSerializer.as_view()),
    path('add_to_cart/', views.add_to_cart )  ,
    path('WishListSerializer/<int:id>/', views.WishListSerializer.as_view())  ,   
    path('WishListSerializer/', views.WishListSerializer.as_view()),
    path('ProductEnter/<int:pk>/', views. ProductEnterDetailSerializer.as_view()) , 
    path('ProductEnterList/', views. ProductEnteredSerializer.as_view()) ,
    path('register_user/', views.register_user),
    path('log_out/', views.log_out),
    path('info/', views.InfoDetailSerializer.as_view()) ,
    path('info/<int:pk>/', views.InfoDetailSerializer.as_view()),
    path('contact/', views.ContacListSerializer.as_view),
    path('contact/<int:pk>/', views. ContactDetailSerializer.as_view())
   
                ]
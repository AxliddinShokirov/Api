from rest_framework import serializers
from Goods.models import *
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields ='__all__'
        depth = 1


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

        depth = 1

class CategoryDetailSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only = True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'title', 'product']


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategoryDetailSerializer(many=True, read_only = True)
    class Meta:
        model = Product
        fields =['id', 'name', 'category', ]

class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'author']
        depth = 1

class WishlistListSerializer(serializers.ModelSerializer):
    product=ProductListSerializer(read_only = True)
    class Meta:
        model =WishList
        fields =[ 'id','product', 'user']
        
class ProductEnterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductEnter
        fields = '__all__'
    
class ProductEnterDetailSerializer(serializers.ModelSerializer):
    product=ProductListSerializer(read_only = True)
    class Meta:
        model = ProductEnter
        fields=['id', 'quantity', 'product']    





       
      



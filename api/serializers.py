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



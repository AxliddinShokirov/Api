from django.contrib.auth import  authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from Goods.models import Product , Category 
from rest_framework.authtoken.models import Token
from api.serializers import *

class ProdactList(generics.ListCreateAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all() 


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()


class CategoryDetailSerializer(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()


class ProductDetailSerializer(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()


@api_view(['POST'])
def log_in(request):
    username=request.data.get('username')
    password=request.data.get('password')
    user= authenticate(username=username,  password=password)
    if user is not None:
        token_key , _ = Token.objects.get_or_create(user=user)
        context={
            'username':user.username,
            'key':token_key.key, 
            'sucsess':True,
        }
    else:
        context={
            'sucsess':False,
        }     
    return Response(context)











    


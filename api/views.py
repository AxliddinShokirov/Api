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


class CartDetailSerializer(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartDetailSerializer
    queryset = Cart.objects.all()


class WishListSerializer(generics.ListCreateAPIView):
    serializer_class =WishlistListSerializer
    queryset = WishList.objects.all()


class ProductEnteredSerializer(generics.ListCreateAPIView):
    serializer_class = ProductEnterDetailSerializer
    queryset = ProductEnter.objects.all()



class ProductEnterDetailSerializer (generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductEnterDetailSerializer
    queryset = ProductEnter.objects.all()


class InfoDetailSerializer(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InfoDetailSerializer
    queryset = Info.objects.all()


class ContacListSerializer(generics.ListCreateAPIView):
     serializer_class = ContactListSerializer
     queryset = Contact.objects.all()

class ContactDetailSerializer(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactDetailSerializer
    queryset = Contact.objects.all()
    

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



@api_view(['POST', 'GET'])
def register_user(request):
    username=request.data.get('username')
    password=request.data.get('password')
    user=User.objects.create_user(username=username, password=password)
    if user.is_authenticated:
        token_key,_ = Token.objects.get_or_create(user=user)
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




@api_view(['POST'])
def log_out(request):
    user=request.user
    if user.is_authenticated:
        user.auth_token.delete()
    return Response({'sucsess':True})




@api_view(['POST'])
def add_to_cart(request):
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity')
    user = request.user
    if user.is_authenticated:
        product = Product.objects.get(id=product_id)
        cart, _ = Cart.objects.get_or_create(author=user, is_active=True)
        cart_product, _ = CartProduct.objects.get_or_create(cart=cart, product=product)
        cart_product.quantity += quantity
        cart_product.total_price += quantity * product.price
        cart_product.save()
        return Response({'sucsess':True})
    else:
        return Response({'sucsess':False})
    












    


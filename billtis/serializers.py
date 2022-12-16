from rest_framework import serializers
from .models import Place, User, Menu, Product, Table

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('pk', 'name', 'place', 'code')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('pk', 'name', 'description', 'price')

class MenuSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ('pk','name', 'place', 'products')
    
    def get_products(self, obj):
        products = Product.objects.filter(menu=obj.id)
        return ProductSerializer(products, many=True).data

class PlaceSerializer(serializers.ModelSerializer):
    menus = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = ('pk', 'name', 'address', 'menus')
    
    def get_menus(self, obj):
        menus = Menu.objects.filter(place=obj.id)            
        return MenuSerializer(menus, many=True).data
    
    

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Place, Table, Menu, Product
from .cart import Cart
from .serializers import *

@api_view(['GET'])
def home(request):
	if request.method == 'GET':
		data = Place.objects.all()
		serializer = PlaceSerializer(data, context={'request': request}, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def place(request, id):
	
	try:
		place = Place.objects.get(id = id)
	except Place.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
	serializer = PlaceSerializer(place)
	return Response(serializer.data)

@api_view(['GET'])
def menu(request, id):

	try:
		menu = Menu.objects.get(id = id)
	except Menu.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
	serializer = MenuSerializer(menu)
	return Response(serializer.data)

@api_view(['GET'])
def product(request, id):

	try:
		product = Product.objects.get(id = id)
	except Product.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	serializer = ProductSerializer(product)
	return Response(serializer.data)
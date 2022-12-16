from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Place(models.Model):
	name = models.CharField(max_length=255)
	address = models.CharField(max_length=255, null=True)

	def __str__(self):
		return f"{self.name} - {self.address}"

class Table(models.Model):
	name = models.CharField(max_length=255)
	place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)
	code = models.IntegerField(null=True)

	def __str__(self):
		return f"{self.name} - {self.place} - {self.code}"

class Menu(models.Model):
	name = models.CharField(max_length=100)
	place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return f"{self.name} - {self.place}"

class Product(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, null=True)
	price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return f"{self.name} - {self.description} - {self.price} - {self.menu}"

from django.db import models
from .customer import Customer
from .product import Product
import datetime

class Order(models.Model):
	customer = models.ForeignKey(Customer,on_delete=models.CASCADE,default='')
	product = models.ForeignKey(Product,on_delete=models.CASCADE,default='')
	quantity = models.IntegerField(default=1)
	price = models.IntegerField(default=0)
	date = models.DateField(default=datetime.datetime.today)
	address = models.CharField(max_length=255,default='')
	phone = models.CharField(max_length=15,default='')
	# payment_mode=models.CharField(max_length=20,blank=True)
	completed = models.BooleanField(default=False)

	
	def __str__(self):
		return self.customer.email
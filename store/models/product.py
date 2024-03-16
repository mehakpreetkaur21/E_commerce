from django.db import models
from .category import Category

class Product(models.Model):
	name = models.CharField(max_length=220,default='')
	keyword = models.CharField(max_length=220,default='')
	price = models.IntegerField(default=0)
	category = models.ForeignKey(Category,on_delete=models.CASCADE,default=None)
	description = models.TextField(default='')
	image1 = models.ImageField(upload_to='upload/products',default='')
	image2 = models.ImageField(upload_to='upload/products',default='')
	image3 = models.ImageField(upload_to='upload/products',default='')
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	# All Product get
	@staticmethod
	def getAllProduct():
		return Product.objects.all()

	# Filter Product By Category
	@staticmethod
	def getProductByFilter(category_id):
		if category_id:
			return Product.objects.filter(category = category_id)
		else:
			return Product.getAllProduct()

	@staticmethod
	def getProductById(productList):
		return Product.objects.filter(id__in=productList)
from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=20,default='')
	image=models.ImageField(upload_to="upload/category",default='')

	def __str__(self):
		return self.name


	@staticmethod
	def getAllCategory():
		return Category.objects.all()
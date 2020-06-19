from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=100)
	phonenumber = models.CharField(max_length=20)
	message = models.TextField(max_length=200)

	def __str__(self):
		return self.name

class  Trick(models.Model):
	sno = models.IntegerField()
	name = models.CharField(max_length=50)
	age = models.IntegerField()

	def __str__(self):
		return self.name


class Register(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	email = models.EmailField(max_length=100)
	password = models.CharField(max_length=100)

	def __str__(self):
		return self.name


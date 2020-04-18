from django.db import models

# Create your models here.
class User(models.Model):
	nama_depan = models.CharField(max_length=30)
	nama_belakang = models.CharField(max_length=20)
	alamat = models.TextField()

	def __str__(self):
		return "{}. {}".format(self.id,self.nama_depan)

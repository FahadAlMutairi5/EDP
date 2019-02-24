from django.db import models
from django.urls import reverse

class ProtModel(models.Model):
	name = models.CharField(max_length=120)
	descri = models.CharField(max_length=220)
	imag = models.ImageField(null=False , blank =False)

	def __str__ (self):
		return self.name

	def get_absolute_url(self):
		return reverse('prot-detail', kwargs={'prot_id':self.id})

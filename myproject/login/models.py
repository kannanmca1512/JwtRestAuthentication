from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Address(models.Model):
	address_line_1 = models.CharField(
		max_length=150, default=None, null=True, blank=True)
	address_line_2 = models.CharField(
		max_length=150, default=None, null=True, blank=True)
	city = models.CharField(
		max_length=150, default=None, null=True, blank=True)
	state = models.CharField(
		max_length=150, default=None, null=True, blank=True)
	country = models.CharField(
		max_length=150, default=None, null=True, blank=True)
	zip_code = models.CharField(
		max_length=150, default=None, null=True, blank=True)
	phone_1 = models.CharField(
		max_length=150, default=None, null=True, blank=True)
	phone_2 = models.CharField(
		max_length=150, default=None, null=True, blank=True)
	fax = models.CharField(max_length=150, default=None, blank=True, null=True)

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	address = models.ForeignKey(Address, on_delete=models.PROTECT, null=True)
	def __str__(self):
	   return self.user.email
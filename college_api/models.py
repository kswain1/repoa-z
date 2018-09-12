from jsonfield import JSONField
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.

class AthleteProfileManager(BaseUserManager):
	"""Helps django work with our customer user model"""

	def create_user(self, email, name, password=None):
		"""create a new user profile"""

		if not email: 
			raise ValueError('Users must have an email address.')

		email = self.normalize_email(email)
		user = self.model(email=email, name=name)

		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_superuser(self, email, name, password):
		"""creates and saves a new superuser with given details"""
		user = self.create_user(email, name, password)
		user.is_superuser = True
		user.is_staff = True
		user.save(using=self._db)

		return user

class AthleteProfile(AbstractBaseUser, PermissionsMixin):
	"""This class is going to represent a user profile inside of our system"""


	email = models.EmailField(max_length=255, unique=True)
	name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	
	#required when creating custom users 
	objects = AthleteProfileManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']

	def get_full_name(self):
		"""Used to get a users full name"""

		return self.name


	def get_short_name(self):
		"""user to get the user first name"""

		return self.name

	def __str__(self):
		"""Django uses this when its need to converts the object into a string"""

		return self.email

class AthleteFeedItem(models.Model):
	"""profile status update"""

	user_profile = models.ForeignKey('AthleteProfile', on_delete=models.CASCADE)
	status_text = models.CharField(max_length=255)
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Returns the model as a string"""

		return self.status_text
 
class AthleteEMGDataItem(models.Model):
	"""Storing of the medical data for athletes"""

	user_profile = models.ForeignKey('AthleteProfile', on_delete=models.CASCADE)
	emg_data = JSONField()
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Returns the model as a string"""

		return self.emg_data



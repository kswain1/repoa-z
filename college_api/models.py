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

class  PlayerTest(models.Model):
	"""Storing of the medical data for athletes"""

	user_profile = models.ForeignKey('AthleteProfile', on_delete=models.CASCADE)
	player_name = models.CharField(max_length=255)
	created_on = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		"""Returns the model as a string"""

		return self.player_name

class Player(models.Model):
	"""player model"""
	trainer_profile = models.ForeignKey('AthleteProfile',on_delete=models.CASCADE)
	player_name = models.CharField(max_length=255)
	team_name = models.ForeignKey('Team', on_delete=models.CASCADE)
	user_age = models.IntegerField()

	def __str__(self):
		"""returns the model as a string"""

		return self.player_name

class Team(models.Model):   
	team_name = models.CharField(max_length=255) #a list of all different teams that are possible

	def __str__(self):
		"""returns the model as a string"""

		return self.team_name

class Medical_Report(models.Model):
	"""Summary medical report for the athlete"""
	player = models.ForeignKey('Player', on_delete=models.CASCADE)
	created_on = models.DateTimeField(auto_now_add=True)
	injuries = models.ForeignKey('Injury', on_delete=models.CASCADE)
	surgeries = models.ForeignKey('Surgery', on_delete=models.CASCADE)
	drug_allergies = models.TextField()
	medications = models.ForeignKey('Medication', on_delete=models.CASCADE)

#Create a model for injuries 
class Injury(models.Model):
	injury_type = models.CharField(max_length=255)
	name = models.CharField(max_length=255)

#Create a model for surgeries 
class Surgery(models.Model):
	s_type = models.CharField(max_length=255)
	name = models.CharField(max_length=255)

#Create a model for medications
class Medication(models.Model):
	name = models.CharField(max_length=255)


class Session(models.Model):
	"""summary ofsession data holder"""
	player = models.ForeignKey('Player', on_delete=models.CASCADE)
	peroneals_rle = JSONField()
	peroneals_lle = JSONField()
	med_gastro_lle = JSONField()
	med_gastro_rle = JSONField()
	tib_anterior_lle = JSONField()
	tib_anterior_rle = JSONField()
	lat_gastro_lle = JSONField()
	lat_gastro_rle = JSONField()
	created_on = models.DateTimeField(auto_now_add=True)
	assessment = models.TextField()
	treatment = models.TextField()	







class AthleteMedSession(models.Model):
	"""Posting the athletes emg data for sessions"""

	user_profile = models.ForeignKey('AthleteProfile',on_delete=models.CASCADE)
	user_age = models.IntegerField()
	profile_image = models.URLField()
	tib_anterior_lle = JSONField()
	tib_anterior_rle = JSONField()
	peroneals_rle = JSONField()
	peroneals_lle = JSONField()
	med_gastro_rle = JSONField()
	med_gastro_lle = JSONField()
	lat_gastro_rle = JSONField()
	lat_gastro_lle = JSONField()
	created_on = models.DateTimeField(auto_now_add=True)
	assessment = models.TextField()
	treatment = models.TextField()

	def __str__(self):
		"""Returns the model with the user id"""

		return self.user_profile

class SessionSummary(models.Model):
	user_profile = models.ForeignKey('AthleteProfile', on_delete=models.CASCADE)
	peroneals_rle = JSONField()
	peroneals_lle = JSONField()
	med_gastro_lle = JSONField()
	med_gastro_rle = JSONField()
	tib_anterior_lle = JSONField()
	tib_anterior_rle = JSONField()
	lat_gastro_lle = JSONField()
	lat_gastro_rle = JSONField()
	created_on = models.DateTimeField(auto_now_add=True)
	assessment = models.TextField()
	treatment = models.TextField()







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

    # required when creating custom users
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


class Player(models.Model):
    """player model"""
    trainer_profile = models.ForeignKey('AthleteProfile', on_delete=models.CASCADE, null=True, blank=True)
    player_name = models.CharField(max_length=255)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True)
    user_age = models.IntegerField()

    def __str__(self):
        """returns method as a string"""

        return self.player_name

    def __unicode__(self):
        """returns player name as a string"""

        return self.player_name


class Team(models.Model):
    """team name"""
    team_name = models.CharField(max_length=255)

    def __str__(self):
        """returns the model as a string name"""

        return self.team_name


class Session(models.Model):
    """summary ofsession data holder"""
    trainer_profile = models.ForeignKey('AthleteProfile', on_delete=models.CASCADE, )
    player_profile = models.ForeignKey('Player', on_delete=models.CASCADE, null=True, blank=True)
    peroneals_rle = JSONField(null=True, blank=True)
    peroneals_lle = JSONField(null=True, blank=True)
    med_gastro_lle = JSONField(null=True, blank=True)
    med_gastro_rle = JSONField(null=True, blank=True)
    tib_anterior_lle = JSONField(null=True, blank=True)
    tib_anterior_rle = JSONField(null=True, blank=True)
    lat_gastro_lle = JSONField(null=True, blank=True)
    lat_gastro_rle = JSONField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    assessment = models.TextField(null=True, blank=True)
    treatment = models.TextField(null=True, blank=True)

class Composite(models.Model):
    """fields for the composite score"""
    player_profile = models.ForeignKey('Player', on_delete=models.CASCADE)
    risk_area = models.ForeignKey('Injury', on_delete=models.CASCADE, null=True, blank=True)
    left_leg_length = models.FloatField(null=True, blank=True)
    right_leg_length = models.FloatField(null=True, blank=True)
    post_medial_direction_rle = models.FloatField(null=True, blank=True)
    post_medial_direction_lle = models.FloatField(null=True, blank=True)
    ant_direction_rle = models.FloatField(null=True, blank=True)
    ant_direction_lle = models.FloatField(null=True, blank=True)
    post_lateral_direction_lle = models.FloatField(null=True, blank=True)
    post_lateral_direction_rle = models.FloatField(null=True, blank=True)
    composite_score_rle = models.FloatField(null=True, blank=True)
    composite_score_lle = models.FloatField(null=True, blank=True)
    assessment = models.TextField(null=True, blank=True)
    treatment = models.TextField(null=True, blank=True)



class Injury(models.Model):
    """list of all the major injuries an athlete can have"""
    name = models.CharField(max_length=255)
    url = models.URLField()


    def __str__(self):
        """returns the model as a string name"""
        return self.name


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


class AthleteMedSession(models.Model):
    """Posting the athletes emg data for sessions"""

    user_profile = models.ForeignKey('AthleteProfile', on_delete=models.CASCADE)
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

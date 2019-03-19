from jsonfield import JSONField
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
import json

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

class UserRole(models.Model):
    """types of user"""
    user_role = models.CharField(max_length=255)

    def __str__(self):
        """returns the user type as a string name"""

        return self.user_role

class Player(models.Model):
    """player model"""
    trainer_profile = models.ForeignKey('AthleteProfile', on_delete=models.CASCADE, null=True, blank=True)
    player_name = models.CharField(max_length=255)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, blank=True)
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

class YBalanceType(models.Model):
    """ Stores the type of Y-Balance Sessions"""
    y_balance_direction = models.CharField(max_length=255)

    def __str__(self):
        """returns the models as a string name"""
        return self.y_balance_direction

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

class SessionLog(models.Model):
    """complete data log of session"""
    trainer_profile = models.ForeignKey('AthleteProfile', on_delete=models.CASCADE,)
    player_profile = models.ForeignKey('Player', on_delete=models.CASCADE, null=True, blank=True)
    time = JSONField(null=-True, blank=True)
    peroneals_rle = JSONField(null=True, blank=True)
    peroneals_lle = JSONField(null=True, blank=True)
    med_gastro_lle = JSONField(null=True, blank=True)
    med_gastro_rle = JSONField(null=True, blank=True)
    tib_anterior_lle = JSONField(null=True, blank=True)
    tib_anterior_rle = JSONField(null=True, blank=True)
    lat_gastro_lle = JSONField(null=True, blank=True)
    lat_gastro_rle = JSONField(null=True, blank=True)
    created_on = models.DateField(auto_now_add=True, null=True, blank=True)
    assessment = models.TextField(null=True, blank=True)
    treatment = models.TextField(null=True, blank=True)

class PlayerProfile(models.Model):
    """stores the summary of a player profile based on signals from mvc and ybalance models"""
    user_id = models.ForeignKey('AthleteProfile', on_delete=models.CASCADE)
    name = models.ForeignKey('Player', on_delete=models.CASCADE)
    peroneals = JSONField(null=True, blank=True, default={"left":
                                                              {"mvc":0,
                                                               "effeciency_score":0,
                                                               "exhaustion":{"maxEffeciency":0,
                                                                             "subMaxEffeciency":0,
                                                                             "minEffeciency":0}},
                                                            "right":
                                                                {"mvc":0,
                                                                 "effeciency_score":0,
                                                                 "exhaustion":{"maxEffeciency":0,
                                                                             "subMaxEffeciency":0,
                                                                             "minEffeciency":0}}
                                                          })
    tib_anterior = JSONField(null=True, blank=True, default={"left":
                                                              {"mvc":0,
                                                               "effeciency_score":0,
                                                               "exhaustion":{"maxEffeciency":0,
                                                                             "subMaxEffeciency":0,
                                                                             "minEffeciency":0}},
                                                            "right":
                                                                {"mvc":0,
                                                                 "effeciency_score":0,
                                                                 "exhaustion":{"maxEffeciency":0,
                                                                             "subMaxEffeciency":0,
                                                                             "minEffeciency":0}}
                                                          })
    lat_gastro = JSONField(null=True, blank=True, default={"left":
                                                              {"mvc":0,
                                                               "effeciency_score":0,
                                                               "exhaustion":{"maxEffeciency":0,
                                                                             "subMaxEffeciency":0,
                                                                             "minEffeciency":0}},
                                                            "right":
                                                                {"mvc":0,
                                                                 "effeciency_score":0,
                                                                 "exhaustion":{"maxEffeciency":0,
                                                                             "subMaxEffeciency":0,
                                                                             "minEffeciency":0}}
                                                          })
    med_gastro = JSONField(null=True, blank=True, default={"left":
                                                              {"mvc": 0,
                                                               "effeciency_score":0,
                                                               "exhaustion": {"maxEffeciency": 0,
                                                                             "subMaxEffeciency": 0,
                                                                             "minEffeciency": 0}},
                                                            "right":
                                                                {"mvc":0,
                                                                 "effeciency_score":0,
                                                                 "exhaustion":{"maxEffeciency":0,
                                                                             "subMaxEffeciency":0,
                                                                             "minEffeciency":0}}
                                                          })


    def __str__(self):
        """returns the name of the athlete"""
        return str(self.name)

class MVCType(models.Model):
    """List of types of MVC sessions"""
    mvc_name = models.CharField(max_length=255)

    def __str__(self):
        """returns the team models as a string"""
        return self.mvc_name

class MVC(models.Model):
    """ Maximum Voltage Contraction (MVC) Amplitude scores for athletes"""
    user_profile = models.ForeignKey('AthleteProfile', on_delete=models.CASCADE)
    player_profile = models.ForeignKey('Player', on_delete=models.CASCADE)
    tib_anterior_lle = models.FloatField(null=True, blank=True)
    tib_anterior_rle = models.FloatField(null=True, blank=True)
    med_gastro_rle = models.FloatField(null=True, blank=True)
    med_gastro_lle = models.FloatField(null=True, blank=True)
    peroneals_lle = models.FloatField(null=True, blank=True)
    peroneals_rle = models.FloatField(null=True, blank=True)
    lat_gastro_lle = models.FloatField(null=True, blank=True)
    lat_gastro_rle = models.FloatField(null=True, blank=True)
    mvc = models.ForeignKey(MVCType, on_delete=models.CASCADE , blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class MVCLog(models.Model):
    """ Maximum Voltage Log Contraction (MVC) Amplitude scores for athletes"""
    user_id = models.ForeignKey('AthleteProfile', on_delete=models.CASCADE)
    player_profile = models.ForeignKey('Player', on_delete=models.CASCADE)
    tib_anterior_lle = JSONField(null=True, blank=True)
    tib_anterior_rle = JSONField(null=True, blank=True)
    med_gastro_rle = JSONField(null=True, blank=True)
    med_gastro_lle = JSONField(null=True, blank=True)
    peroneals_lle = JSONField(null=True, blank=True)
    peroneals_rle = JSONField(null=True, blank=True)
    lat_gastro_lle = JSONField(null=True, blank=True)
    lat_gastro_rle = JSONField(null=True, blank=True)
    mvc = models.ForeignKey(MVCType, on_delete=models.CASCADE, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)


##step 1 updating mvc data
## step updated playerPorfile scores model
 ##run for loop for all of the fields, and update playerProfilemodel
["tib_anterior", "med_gastro", "peroneals", "lat_gastro"]
@receiver(post_save, sender=MVCLog)
def update_mvc_player(sender, **kwargs):
    if kwargs.get('created', False):
        checkPlayer = PlayerProfile.objects.filter(name_id=kwargs['instance'].player_profile.id).first()
        #create the object
        if not checkPlayer:
            checkPlayer = PlayerProfile.objects.create(name_id=kwargs['instance'].player_profile.id,
                                               user_id_id=kwargs['instance'].user_id.id)
        updatePlayerProfile(kwargs['instance'],checkPlayer)


def updatePlayerProfile(instance, playerProfile):
    muscles = ["tib_anterior", "med_gastro", "peroneals", "lat_gastro"]

    ##MVC Updates
    for i in muscles:
        ## field is set to be our player profile muscle field
        if getattr(instance, i + "_lle") != "":
            field = getattr(playerProfile, i)
            field["left"]["mvc"] = getattr(instance, i + "_lle")
        if getattr(instance, i + "_rle") != "":
            field = getattr(playerProfile, i)
            field["right"]["mvc"] = getattr(instance, i + "_rle")

    playerProfile.save()


@receiver(post_save, sender=Session)
def update_ybal_player(sender, **kwargs):
    if kwargs.get('created', False):
        checkPlayer = PlayerProfile.objects.filter(name_id=kwargs['instance'].player_profile.id).first()

        if not checkPlayer:
            checkPlayer = PlayerProfile.objects.create(name_id=kwargs['instance'].player_profile.id,
                                                       user_id_id=kwargs['instance'].trainer_profile.id)
    updateYbalPlayerProfile(kwargs['instance'], checkPlayer)

def updateYbalPlayerProfile(instance, playerProfile):
    muscles = ["tib_anterior", "med_gastro", "peroneals", "lat_gastro"]

    ##MVC Updates
    for muscle in muscles:
        ## field is set to be our player profile muscle field
        #import pdb; pdb.set_trace()
        if getattr(instance , muscle+"_lle") != "":
            field = getattr(playerProfile, muscle)
            # field = json.loads(field.replace("'", '"'))

            if isinstance(field,str):
                field = json.loads(field.replace("'", '"'))

            ##Fix in the future
            if field["left"]["mvc"]:
                effeciency = sum(json.loads(getattr(instance, muscle +"_lle")))/len(json.loads(getattr(instance, muscle +"_lle")))
                effeciency = (effeciency/float(field["left"]["mvc"])) * 100

                emg_data = json.loads(getattr(instance, muscle + "_lle"))
                mvc = float(field["left"]["mvc"])
                maxCounter = 0
                subMaxCounter = 0
                minCounter = 0

                for i in range(0, len(emg_data)):
                    if emg_data[i] >=  (mvc* .70):
                       maxCounter += 1
                    elif emg_data[i] >= (mvc* .50):
                        subMaxCounter += 1
                    else:
                        minCounter += 1

                #import pdb; pdb.set_trace()
                maxEffeciency = (maxCounter/len(emg_data)) * 100
                subMaxEffeciency = (subMaxCounter/len(emg_data)) * 100
                minEffeciency = (minCounter/len(emg_data)) * 100

                field["left"]["effeciency_score"] = effeciency
                field["left"]["exhaustion"] = {"maxEffeciency":maxEffeciency,"subMaxEffeciency":subMaxEffeciency,"minEffeciency":minEffeciency}

        if getattr(instance , muscle+"_rle") != "":

            field = getattr(playerProfile, muscle)

            if isinstance(field,str):
                field = json.loads(field.replace("'", '"'))

            # field = json.loads(field.replace("'", '"'))

            ##Fix in the future
            #import pdb; pdb.set_trace()
            if field["right"]["mvc"]:
                effeciency = sum(json.loads(getattr(instance, muscle + "_rle"))) / len(json.loads(getattr(instance, muscle + "_rle")))
                effeciency = (effeciency / float(field["right"]["mvc"])) * 100

                emg_data = json.loads(getattr(instance, muscle + "_rle"))
                mvc = float(field["right"]["mvc"])
                maxCounter = 0
                subMaxCounter = 0
                minCounter = 0

                for i in range(0, len(emg_data)):
                    if emg_data[i] >= (mvc * .70):
                        maxCounter += 1
                    elif emg_data[i] >= (mvc * .50):
                        subMaxCounter += 1
                    else:
                        minCounter += 1

                #import pdb; pdb.set_trace()
                maxEffeciency = (maxCounter / len(emg_data)) * 100
                subMaxEffeciency = (subMaxCounter / len(emg_data)) * 100
                minEffeciency = (minCounter / len(emg_data)) * 100

                #import pdb; pdb.set_trace()
                field["right"]["effeciency_score"] = effeciency
                field["right"]["exhaustion"] = {"maxEffeciency":maxEffeciency,"subMaxEffeciency":subMaxEffeciency,"minEffeciency":minEffeciency}

    ##YbalUpdates
    playerProfile.save()

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
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """returns the model as a string name"""

        return self.player_profile


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
    player_profile = models.ForeignKey('Player', on_delete=models.CASCADE, null=True, blank=True)
    tib_anterior_lle = JSONField()
    tib_anterior_rle = JSONField()
    peroneals_rle = JSONField()
    peroneals_lle = JSONField()
    med_gastro_rle = JSONField()
    med_gastro_lle = JSONField()
    lat_gastro_rle = JSONField()
    lat_gastro_lle = JSONField()
    created_on = models.DateTimeField(auto_now_add=True)
    assessment = models.TextField(null=True, blank=True)
    treatment = models.TextField(null=True, blank=True)
    user_age = models.IntegerField()

    def __str__(self):
        """Returns the model with the user id"""

        return self.user_profile

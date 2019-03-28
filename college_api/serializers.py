from rest_framework import serializers
import json
from . import models


class HelloSerializer(serializers.Serializer):
    """serializes a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)


class AthleteProfileSerializer(serializers.ModelSerializer):
    """A  serializer fro our user profile objects"""

    class Meta:
        model = models.AthleteProfile
        fields = ('id', 'email', 'name', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user"""

        user = models.AthleteProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class UserRole(serializers.ModelSerializer):
    """roles of the different types of user"""

    class Meta:
        model = models.UserRole
        fields = ('id', 'user_role')



class Team(serializers.ModelSerializer):
    """ for creating teams for the model"""

    class Meta:
        model = models.Team
        fields = ('id', 'team_name',)


class Player(serializers.ModelSerializer):
    """a serializer table for working with the player"""
    #team = Team()

    class Meta:
        model = models.Player
        fields = ('id', 'trainer_profile', 'player_name',
                  'team', 'team_id','user_age',)
        extra_kwargs = {'trainer_profile': {'read_only': True}}


class ShortPlayer(serializers.ModelSerializer):
    class Meta:
        model = models.Player
        fields = ('player_name',)


class Session(serializers.ModelSerializer):
    """Serialzier for the sessions"""
    user_name = serializers.CharField(source='Session.players.player_name', read_only=True)

    # player_profile = ShortPlayer(many=False)

    class Meta:
        model = models.Session
        fields = ('id', 'trainer_profile', 'user_name', 'player_profile', 'peroneals_rle', 'peroneals_lle',
                  'med_gastro_lle',
                  'med_gastro_rle', 'tib_anterior_lle', 'tib_anterior_rle', 'lat_gastro_lle', 'lat_gastro_rle',
                  'created_on', 'assessment', 'treatment')
        extra_kwargs = {'trainer_profile': {'read_only': True}}


class CompositeScore(serializers.ModelSerializer):
    """serializer for the composite score bar"""

    class Meta:
        model = models.CompositeScore
        fields = ('id','user','name','leg_length_rle', 'leg_length_lle','anterior_rle','anterior_lle',
                  'posterior_medial_rle', 'posterior_medial_lle','posterior_lateral_lle','posterior_lateral_rle')
        extra_kwargs = {'user':{'read_only':True}}



class Composite(serializers.ModelSerializer):
   """serializer for the composite and y-balance data"""

   class Meta:
        model = models.Composite
        fields = ('id','player_profile','risk_area','left_leg_length','right_leg_length','post_medial_direction_rle','post_medial_direction_lle',
                 'ant_direction_rle','ant_direction_lle','post_lateral_direction_lle','post_lateral_direction_rle',
                 'composite_score_lle','composite_score_rle','assessment','treatment', 'created_on')

class SessionLog(serializers.ModelSerializer):
    """full data for the session log information"""
    user_name = serializers.CharField(source='Session.players.player_name', read_only=True)

    class Meta:
        model = models.SessionLog
        fields = ('id', 'trainer_profile', 'user_name', 'player_profile', 'peroneals_rle', 'peroneals_lle', 'med_gastro_lle',
                  'med_gastro_rle', 'tib_anterior_lle', 'tib_anterior_rle', 'lat_gastro_lle', 'lat_gastro_rle',
                  'created_on', 'assessment', 'treatment','time')
        extra_kwargs = {'trainer_profile': {'read_only': True}}



class Injury(serializers.ModelSerializer):
    """serializer for the injury models"""

    class Meta:
        model = models.Injury
        fields = ('id','name','url')


    # 'player_profile__user_age'

# def create(self, validated_data):
# 	player_data = validated_data.pop('player')
# 	player = Player.create(Player(), validated_data=player_data)
# 	new_player_name = models.Session.create(player=player, **validated_data)
# 	return new_player_name


class AthleteFeedItemSerializer(serializers.ModelSerializer):
    """A serializer for profile feed items"""

    class Meta:
        model = models.AthleteFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}


class AthleteEMGDataSerializer(serializers.ModelSerializer):
    """ a serlizer to review the emg data of athletes"""

    class Meta:
        model = models.AthleteEMGDataItem
        fields = ('id', 'user_profile', 'emg_data', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}


class AthleteMedSessionSerializer(serializers.ModelSerializer):
    """a serilizer for the post of athlete emg data"""

    class Meta:
        model = models.AthleteMedSession
        fields = ('id', 'user_profile', 'user_age', 'tib_anterior_lle', 'tib_anterior_rle',
                  'peroneals_rle', 'peroneals_rle', 'peroneals_lle', 'med_gastro_rle',
                  'med_gastro_lle', 'lat_gastro_rle', 'lat_gastro_lle', 'created_on',
                  'assessment', 'treatment')
        extra_kwargs = {'user_profile': {'read_only': True}}

class MVCSerializer(serializers.ModelSerializer):
    """A serializer for posting MVC data from the EMG"""

    class Meta:
        model = models.MVC
        fields = ('id', 'user_profile', 'player_profile', 'tib_anterior_lle', 'tib_anterior_rle', 'med_gastro_lle',
                  'med_gastro_rle','peroneals_lle', 'peroneals_rle', 'lat_gastro_rle', 'lat_gastro_lle', 'mvc',
                  'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
class MVCLogSerializer(serializers.ModelSerializer):
    """A serializer for posting MVC Log data from the EMG"""

    class Meta:
        model = models.MVCLog
        fields = ('id', 'user_id', 'player_profile', 'tib_anterior_lle','tib_anterior_rle', 'med_gastro_lle', 'med_gastro_rle',
                  'peroneals_lle','peroneals_rle','lat_gastro_lle','lat_gastro_rle','mvc','created_on')
        extra_kwargs = {'user_id': {'read_only':True}}

class MVCType(serializers.ModelSerializer):
    """A serializer for the different types of MVC data collection"""

    class Meta:
        model = models.MVCType
        fields = ('id', 'mvc_name')



class PlayerProfileSerializer(serializers.ModelSerializer):
    """a serializer for player objects"""

    class Meta:
        model = models.PlayerProfile
        fields = ('id', 'user_id', 'name','leg_length_rle', 'leg_length_lle', 'anterior_rle', 'anterior_lle',
                  'posterior_medial_rle', 'posterior_medial_lle', 'posterior_lateral_rle', 'posterior_lateral_lle',
                  'composite_score_lle', 'composite_score_rle', 'med_gastro', 'lat_gastro', 'tib_anterior', 'peroneals')
        extra_kwargs = {'user_id':{'read_only':True}}

    # def get_med_gastro(self, value):
    #     muscle_data = json.loads(value.med_gastro)
    #     print("Hello we made it here")
    #     return muscle_data

    def to_representation(self, instance):
        muscles = ["med_gastro","lat_gastro","tib_anterior","peroneals"]
        muscle_data = super().to_representation(instance)
        print(muscle_data)
        for muscle in muscles:
            if muscle_data[muscle]:
                muscle_data[muscle] = json.loads(muscle_data[muscle].replace("'",'"'))  #replacing single quotes with double quotes
        return muscle_data

    def get_user_id(self):
        print("we are int he user id field")

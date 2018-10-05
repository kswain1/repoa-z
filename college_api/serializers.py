from rest_framework import serializers

from . import models 

class HelloSerializer(serializers.Serializer):
	"""serializes a name field for testing our APIView"""

	name = serializers.CharField(max_length=10)



class AthleteProfileSerializer(serializers.ModelSerializer):
	"""A  serializer fro our user profile objects"""


	class Meta: 
		model = models.AthleteProfile 
		fields = ('id','email','name','password',)
		extra_kwargs = {'password':{'write_only': True}}

	def create(self, validated_data):
		"""Create and return a new user"""

		user = models.AthleteProfile(
			email = validated_data['email'],
			name = validated_data['name']
			)

		user.set_password(validated_data['password'])
		user.save()

		return user


class Team(serializers.ModelSerializer):
	""" for creating teams for the model"""

	class Meta: 
		model = models.Team
		fields = ('id','team_name',)

class Player(serializers.ModelSerializer):
    """a serializer table for working with the player"""
    #team_name = serializers.StringRelatedField(many=False, source='team')
    team = Team()

    class Meta:
        model = models.Player
        fields =('id','trainer_profile','player_name','team','user_age',)
        extra_kwargs = {'trainer_profile':{'read_only':True}}

class Session(serializers.ModelSerializer):
	"""Serialzier for the sessions"""
	user_name = serializers.CharField(source='Session.players.player_name', read_only=True)

	class Meta: 
		model = models.Session
		fields = ('trainer_profile', 'user_name', 'player_profile','peroneals_rle','peroneals_lle','med_gastro_lle',
			'med_gastro_rle','tib_anterior_lle','tib_anterior_rle','lat_gastro_lle','lat_gastro_rle',
			'created_on','assessment','treatment')
		extra_kwargs = {'trainer_profile':{'read_only':True}}


class AthleteFeedItemSerializer(serializers.ModelSerializer):
	"""A serializer for profile feed items"""

	class Meta:
		model = models.AthleteFeedItem
		fields = ('id', 'user_profile', 'status_text', 'created_on')
		extra_kwargs = {'user_profile': {'read_only':True}}

class AthleteEMGDataSerializer(serializers.ModelSerializer):
	""" a serlizer to review the emg data of athletes"""

	class Meta:
		model = models.AthleteEMGDataItem
		fields = ('id', 'user_profile', 'emg_data', 'created_on')
		extra_kwargs = {'user_profile': {'read_only':True}}

class AthleteMedSessionSerializer(serializers.ModelSerializer):
	"""a serilizer for the post of athlete emg data"""

	class Meta: 
		model = models.AthleteMedSession
		fields = ('id','user_profile','user_age','tib_anterior_lle','tib_anterior_rle',
			'peroneals_rle','peroneals_rle','peroneals_lle', 'med_gastro_rle',
			'med_gastro_lle','lat_gastro_rle','lat_gastro_lle', 'created_on',
			'assessment','treatment')
		extra_kwargs = {'user_profile': {'read_only':True}}





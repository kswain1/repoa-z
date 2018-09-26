from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from . import models 

class HelloSerializer(serializers.Serializer):
	"""serializes a name field for testing our APIView"""

	name = serializers.CharField(max_length=10)



class AthleteProfileSerializer(serializers.ModelSerializer):
	"""A  serializer fro our user profile objects"""
	username = serializers.CharField(validators=[UniqueValidator(queryset=models.AthleteProfile.objects.all())])
	email = serializers.EmailField(validators=[UniqueValidator(queryset=models.AthleteProfile.objects.all())])

	class Meta: 
		model = models.AthleteProfile 
		fields = ('id','username','name','password',)
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

class PlayerTest(serializers.ModelSerializer):
	class Meta:
		model = models.PlayerTest
		fields = ('id','trainer_profile','player_name','created_on')
		extra_kwargs = {'trainer_profile':{'read_only':True}}


class AthleteMedSessionSerializer(serializers.ModelSerializer):
	"""a serilizer for the post of athlete emg data"""

	class Meta: 
		model = models.AthleteMedSession
		fields = ('id','user_profile','user_age','tib_anterior_lle','tib_anterior_rle',
			'peroneals_rle','peroneals_rle','peroneals_lle', 'med_gastro_rle',
			'med_gastro_lle','lat_gastro_rle','lat_gastro_lle', 'created_on',
			'assessment','treatment')
		extra_kwargs = {'user_profile': {'read_only':True}}



class Player(serializers.ModelSerializer):
	"""a serializer for creating new players"""
	class Meta:
		model = models.Player
		fields = ('trainer_profile','player_name','team_name')
		extra_kwargs = {'trainer_profile':{'read_only':True}}

class MedicalReport(serializers.ModelSerializer):
	"""Medical Report for players"""
	class Meta:
		model = models.Medical_Report
		fields = ('player_id','user_age','created_on','injuries','surgeries','drug_allergies','medications')
		extra_kwargs = {'player_id': {'read_only':True}}

class Session(serializers.ModelSerializer):
	"""Summary medical report for the athlete"""
	class Meta:
		model = models.Session
		fields = ('player','peroneals_rle','peroneals_lle','med_gastro_lle','med_gastro_rle',
			'tib_anterior_lle','tib_anterior_rle','lat_gastro_lle','lat_gastro_rle',
			'created_on','assessment','treatment',)
		extra_kwargs = {'player_id':{'read_only':True}}

class Team(serializers.ModelSerializer):
	"""Serializer """
	class Meta:
		model = models.Team
		fields = ('team_name',)
		extra_kwargs = {'id':{'read_only':True}}





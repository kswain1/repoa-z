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
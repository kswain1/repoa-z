from rest_framework import serializers

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
        fields = ('id','trainer_profile', 'user_name', 'player_profile', 'peroneals_rle', 'peroneals_lle', 'med_gastro_lle',
                  'med_gastro_rle', 'tib_anterior_lle', 'tib_anterior_rle', 'lat_gastro_lle', 'lat_gastro_rle',
                  'created_on', 'assessment', 'treatment')
        extra_kwargs = {'trainer_profile': {'read_only': True}}

class Composite(serializers.ModelSerializer):
   """serializer for the composite and y-balance data"""

   class Meta:
        model = models.Composite
        fields = ('id','player_profile','risk_area','left_leg_length','right_leg_length','post_medial_direction_rle','post_medial_direction_lle',
                 'ant_direction_rle','ant_direction_lle','post_lateral_direction_lle','post_lateral_direction_rle',
                 'composite_score_lle','composite_score_rle','assessment','treatment', 'created_on')


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

import pytest
from django_dynamic_fixture import G

from college_api.models import MVCLog, AthleteProfile, Player, PlayerProfile


@pytest.mark.django_db
def test_create_mvc_log(trainer, trainer_client):
    for c, email in enumerate(['p1@test.com', 'p2@test.com'], 1):
        # Create a related athlete profile
        ap = AthleteProfile.objects.create_user(
            name='Test player',
            email=email,
            password='testpass',
        )
        p = G(Player,
              player_name='Test player',
              trainer_profile=trainer)
        # Create the player profile
        pp = G(
            PlayerProfile,
            user_id=ap,
            name=p,
        )
        for muscle in ['peroneals', 'tib_anterior', 'lat_gastro', 'med_gastro']:
            getattr(pp, muscle)['left']['mvc'] = 15000
            getattr(pp, muscle)['right']['mvc'] = 15000
        pp.save()

        data = {
            'player_profile': p.id,
            'peroneals_rle': 1 * c,
            'peroneals_lle': 1 * c,
            'med_gastro_rle': 2 * c,
            'med_gastro_lle': 2 * c,
            'tib_anterior_lle': 3 * c,
            'tib_anterior_rle': 3 * c,
            'lat_gastro_lle': 4 * c,
            'lat_gastro_rle': 4 * c,
        }
        response = trainer_client.post('/api/mvclog/', data)
        assert response.status_code == 201

        qs = MVCLog.objects.filter(player_profile=player)
        assert qs.count() == 1

        player_profile = player.playerprofile_set.first()
        profile_muscle = muscle[:-4]

        # Testing MVC
        for i, muscle in enumerate(['peroneals', 'med_gastro', 'tib_anterior', 'lat_gastro'], 1):
            assert getattr(player_profile, muscle)['right']['mvc'] == i * c
            assert getattr(player_profile, muscle)['left']['mvc'] == i * c

import random
import pytest


from college_api.models import Session


@pytest.mark.django_db
@pytest.mark.parametrize('muscle', [
    'peroneals_rle',
    'peroneals_lle',
    'med_gastro_rle',
    'med_gastro_lle',
    'tib_anterior_lle',
    'tib_anterior_rle',
    'lat_gastro_lle',
    'lat_gastro_rle',
])
def test_create_session(player, trainer, trainer_client, muscle):
    # Create random readings
    readings = random.sample(range(50), 5)
    readings_str = '[{}]'.format(','.join(map(str, readings)))

    data = {
        'player_profile': player.id,
        muscle: readings_str,
        'assessment': 'test',
        'treatment': 'test'
    }
    response = trainer_client.post('/api/session/', data)
    assert response.status_code == 201, response.content

    qs = Session.objects.all()
    assert qs.count() == 1
    session = qs.first()
    assert session.trainer_profile.id == player.trainer_profile.id
    assert getattr(session, muscle) == readings_str

    side_map = {
        'rle': 'right',
        'lle': 'left'
    }

    player_profile = player.playerprofile_set.first()
    profile_muscle = muscle[:-4]
    side = muscle[-3:]

    muscle_data = getattr(player_profile, profile_muscle)
    side_data = muscle_data[side_map[side]]
    # Testing effeciency score
    effeciency = sum(readings) / float(len(readings))
    score = effeciency / float(15000) * 100.0
    assert side_data['effeciency_score'] == score

    # Testing exhaustion
    exhaustion_data = side_data['exhaustion']
    max_effeciency = len(filter(lambda r: r >= 0.7, readings)) / float(len(readings)) * 100
    submax_effeciency = len(filter(lambda r: 0.5 <= r < 0.7, readings)) / float(len(readings)) * 100
    min_effeciency = len(filter(lambda r: 0.0 <= r < 0.5, readings)) / float(len(readings)) * 100
    assert exhaustion_data['maxEffeciency'] == max_effeciency
    assert exhaustion_data['subMaxEffeciency'] == submax_effeciency
    assert exhaustion_data['minEffeciency'] == min_effeciency

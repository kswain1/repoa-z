import pytest
from django_dynamic_fixture import G, F
from django.test import Client

from college_api.models import Player, PlayerProfile, AthleteProfile


@pytest.fixture
def trainer():
    return AthleteProfile.objects.create_user(
        name='Test trainer',
        email='trainer@test.com',
        password='testpass',
    )


@pytest.fixture
def player(trainer):
    # Create a related athlete profile
    ap = AthleteProfile.objects.create_user(
        name='Test player',
        email='test@test.com',
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
    return p


@pytest.fixture
def trainer_client(player, client):
    """
    A client authenticated as the trainer
    """
    response = client.post('/api/login/', {'username': 'trainer@test.com', 'password': 'testpass'})
    headers = {
        'HTTP_AUTHORIZATION': 'Token {}'.format(response.json()['token']),
        'HTTP_CONTENT_TYPE': 'application/json'
    }
    return Client(**headers)

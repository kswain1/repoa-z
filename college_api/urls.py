from django.conf.urls import url
from django.conf.urls import include 

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset',views.HelloWorldViewSet, base_name='hello-viewset')
router.register('profile', views.AthleteProfileViewSet)
router.register('feed', views.AthleteFeedViewSet)
router.register('emg',views.AthleteEmgData)
router.register('medsession',views.AthleteMedSessionData)
router.register('login', views.LoginViewSet, base_name='login')
router.register('player', views.Player, base_name='Players')
router.register('Session',views.Session)
router.register('Team', views.Team)

router.register('playerTest',views.PlayerTest, base_name='layerTest')
router.register('profile',views.Player, base_name='players')


urlpatterns = [
	url(r'^helloworld/', views.HelloWorldView.as_view()),
	url(r'',include(router.urls))

]
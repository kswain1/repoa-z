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
router.register('player', views.Player)
router.register('team', views.Team)
router.register('session',views.Session)
router.register('injury', views.Injury)


urlpatterns = [
	url(r'^helloworld/', views.HelloWorldView.as_view()),
	url(r'',include(router.urls))

]
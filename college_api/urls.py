from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloWorldViewSet, base_name='hello-viewset')
router.register('profile', views.AthleteProfileViewSet)
router.register('feed', views.AthleteFeedViewSet)
router.register('emg', views.AthleteEmgData)
router.register('medsession', views.AthleteMedSessionData)
router.register('login', views.LoginViewSet, base_name='login')
router.register('player', views.Player)
router.register('team', views.Team)
router.register('session', views.Session)
router.register('sessionlog', views.SessionLog)
router.register('injury', views.Injury)
router.register('composite', views.Composite)
router.register('mvc', views.MVCData)
# router.register('playerdashboard', views.PlayerDashboard, base_name='playerdashboard')
router.register('mvctype', views.MVCTypeViewSet, base_name='mvctype')
router.register('mvclog', views.MVCLogViewSet, base_name='mvclog')
router.register('userrole', views.UserRoleViewSet)
router.register('playerprofile', views.PlayerProfileViewSet)
router.register('compositescore', views.CompositeScore)
# router.register('playerinjury', views.PlayerInjuryDashboard, base_name='playerinjury')

# router_simple = SimpleRouter()
# router_simple.register('playerdashboard', views.PlayerDashboard, base_name='playerdashboard')

urlpatterns = [
    url(r'^helloworld/', views.HelloWorldView.as_view()),
    url(r'', include(router.urls)),
    # url(r'', include(router_simple.urls)),
    url(r'^playerinjury/', views.PlayerInjuryDashboard.as_view())

]

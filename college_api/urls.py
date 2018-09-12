from django.conf.urls import url
from django.conf.urls import include 

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset',views.HelloWorldViewSet, base_name='hello-viewset')
router.register('profile', views.AthleteProfileViewSet)
router.register('feed', views.AthleteFeedViewSet)
router.register('emg',views.AthleteEmgData)


urlpatterns = [
	url(r'^helloworld/', views.HelloWorldView.as_view()),
	url(r'',include(router.urls))

]
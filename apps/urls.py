# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers
from .views import CardTypeViewSet, CardViewSet

router = routers.DefaultRouter()
router.register(r'card', CardViewSet)
router.register(r'cardstype', CardTypeViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


   
from django.urls import path, include
from rest_framework import routers
from . import viewsets


router = routers.DefaultRouter()
router.register(r'property', viewsets.PropertyViewSet)
router.register(r'coordinate', viewsets.CoordinateViewSet)
router.register(r'houmer', viewsets.HoumerViewSet)
router.register(r'houmeradvicer', viewsets.HoumerAdvicerViewSet)
router.register(r'visit', viewsets.VisitViewSet)


urlpatterns = [
    path(r'', include(router.urls))
]
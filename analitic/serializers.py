from rest_framework import serializers
from analitic.models import Property,Coordinate,Houmer,HoumerAdviser,Visit

class PropertySerializer(serializers.Serializer):
    class Meta:
        model = Property
        fields = ['title', 'description', 'latitude', 'length', 'address']

class CoordinateSerializer(serializers.Serializer):
    class Meta:
        model = Coordinate
        fields = ['latitude', 'length', 'timestamp', 'houmer']

class HoumerSerializer(serializers.Serializer):
    class Meta:
        model = Houmer
        fields = ['username']

class HoumerAdviserSerializer(serializers.Serializer):
    class Meta:
        model = HoumerAdviser
        fields = ['username']
        
class VisitSerializer(serializers.Serializer):
    class Meta:
        model = Visit
        fields = ['houmer', 'advicer', 'property', 'timestamp_checkin', 'timestamp_checkout']


from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from analitic.models import Property,Coordinate,Houmer,HoumerAdviser,Visit
from analitic.serializers import PropertySerializer, CoordinateSerializer, HoumerSerializer, HoumerAdviserSerializer, VisitSerializer
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime
from geopy.distance import geodesic

class PropertyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Property to be viewed or edited.
    """
    queryset = Property.objects.all().order_by('-id')
    serializer_class = PropertySerializer
    permission_classes = [permissions.AllowAny]
    
class CoordinateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Coordinate to be viewed or edited.
    """
    queryset = Coordinate.objects.all().order_by('-id')
    serializer_class = CoordinateSerializer
    permission_classes = [permissions.AllowAny]
    
    @action(detail=False, methods=['get'])
    def obtein_coordenates_velocity(self, request):
        """[summary]

        Args:
            request ([get]): [obtain the moments where the input velocity is higher]
            [velocity]: [km/h]
            [date]: [str %Y-%m-%d]
            [houmer]: [str]
        Returns:
            [json]: [time_start,time_end,velocity]
        """
        velocity = request.GET.get('velocity') 
        houmer_input = request.GET.get('houmer')
        date_input = request.GET.get('date')
        date = datetime.strptime(date_input, '%Y-%m-%d')
        houmer = Houmer.objects.filter(username=houmer_input).first()
        if houmer:
            coordinates = Coordinate.objects.filter(houmer=houmer.id)
            coordinates_day = coordinates.filter(timestamp__day=date.day,timestamp__month=date.month,timestamp__year=date.year).order_by('id')
            result = []
            for index in range(len(coordinates_day)-1):
                dif_time = (coordinates_day[index+1].timestamp - coordinates_day[index].timestamp).seconds
                dif_distance = geodesic(
                    (coordinates_day[index+1].latitude,coordinates_day[index+1].length),
                    (coordinates_day[index].latitude,coordinates_day[index].length)
                    ).km 
                velocity_dif = dif_distance/(dif_time/3600)
                if velocity_dif > float(velocity):
                    result.append({
                        "time_start": coordinates_day[index].timestamp,
                        "time_end": coordinates_day[index+1].timestamp,
                        "velocity": velocity_dif,
                        })         
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response([], status=status.HTTP_400_BAD_REQUEST)

    
class HoumerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Houmer to be viewed or edited.
    """
    queryset = Houmer.objects.all().order_by('-id')
    serializer_class = HoumerSerializer
    permission_classes = [permissions.AllowAny]
    
class HoumerAdvicerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Houmer Advicer to be viewed or edited.
    """
    queryset = HoumerAdviser.objects.all().order_by('-id')
    serializer_class = HoumerAdviserSerializer
    permission_classes = [permissions.AllowAny]
    
class VisitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Visit to be viewed or edited.
    """
    queryset = Visit.objects.all().order_by('-id')
    serializer_class = VisitSerializer
    permission_classes = [permissions.AllowAny]
    
    @action(detail=False, methods=['get'])
    def obtein_visits(self, request):
        """[summary]

        Args:
            request ([get]): [get the properties with the duration of the visits]
            [date]: [str %Y-%m-%d]
            [houmer]: [str]
        Returns:
            [json]: [property_id,property_title,visit_duration,latitude,length∫]
        """
        date_input = request.GET.get('date')
        houmer_input = request.GET.get('houmer')
        houmer = Houmer.objects.filter(username=houmer_input).first()
        if houmer:
            visits = Visit.objects.filter(houmer = houmer.id)
            date = datetime.strptime(date_input, '%Y-%m-%d')
            visits_day = visits.filter(timestamp_checkin__day=date.day,timestamp_checkin__month=date.month,timestamp_checkin__year=date.year)
            result = []
            for v in visits_day:
                dif_time = ((v.timestamp_checkout - v.timestamp_checkin).seconds)/3600
                result.append({
                    "property_id": v.property.id ,
                    "property_title": v.property.title,
                    "visit_duration": dif_time,
                    "latitude": v.property.latitude,
                    "length" : v.property.length
                    }) 
                
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response([], status=status.HTTP_400_BAD_REQUEST)
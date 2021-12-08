from django.db import models

# Models describe Property. Must be more atributes in the real life.
class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    latitude = models.FloatField()
    length = models.FloatField()
    address = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'
        unique_together = ('latitude','length','address')

# Models describe Houmer. Must be more atributes in the real life.
class Houmer(models.Model):
    username = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Houmer'
        verbose_name_plural = 'Houmers'

# Models describe Houmer Adviser that shows properties. Must be more atributes in the real life.
class HoumerAdviser(models.Model):
    username = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Houmer Adviser'
        verbose_name_plural = 'Houmer Advicers'

# Models describe the location of Houmer in time
class Coordinate(models.Model):
    latitude = models.FloatField()
    length = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    houmer = models.ForeignKey(Houmer, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Coordinate'
        verbose_name_plural = 'Coordinates'


# Models describe the scheduled visit
class Visit(models.Model):
    houmer = models.ForeignKey(Houmer,on_delete=models.CASCADE)
    advicer = models.ForeignKey(HoumerAdviser,on_delete=models.CASCADE)
    property = models.ForeignKey(Property,on_delete=models.CASCADE)
    timestamp_checkin = models.DateTimeField(blank=True, null=True)
    timestamp_checkout = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'Visit'
        verbose_name_plural = 'Visits'


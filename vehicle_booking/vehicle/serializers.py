
from django.contrib.auth.models import User, Group

from rest_framework import serializers
from vehicle.models import Vehicle, Driver, RequisitionTicketLog

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Group
        fields = ('url','name')


class VehicleSerializer(serializers.ModelSerializer):
    vehicles = serializers.SerializerMethodField(source='get_vehicles')

    class Meta:
        model = Vehicle
        fields = ('vehicle_id','vehicle_number','type','driver_id','status','vehicles')

    def get_vehicles(self, obj):
        '''
            Get title as user full name
        '''
        return 'testdata'

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('driver_id','name','mobile','address','created_at')

"""
requisitionTicketLogId = models.AutoField(primary_key=True)
    type = models.CharField(max_length=8, choices=VEHICLE_TYPES)
    origin = models.CharField(max_length=255, blank=False)
    destination = models.CharField(max_length=255, blank=False)
    driverId = models.ForeignKey('Driver', blank=True)
    ticketStatus = models.CharField(max_length=10, choices=REQUISITION_TICKET_TYPES, default=Submitted)
    note = models.CharField(max_length=255, blank=True)
    fromDateTime = models.DateTimeField(blank=False)
    toDateTime = models.DateTimeField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
"""


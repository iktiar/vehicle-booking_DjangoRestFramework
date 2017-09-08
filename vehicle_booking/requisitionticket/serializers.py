from django.contrib.auth.models import User, Group

from rest_framework.serializers import ModelSerializer, SerializerMethodField, PrimaryKeyRelatedField
from vehicle.models import RequisitionTicketLog, Vehicle
from vehicle.serializers import   VehicleSerializer


class RequisitionTicketLogListSerializer(ModelSerializer):
    #driverId = SerializerMethodField()

    class Meta:
        model = RequisitionTicketLog
        fields = ('requisitionTicketLog_id', 'vehicle_id', 'vehicle_number','vehicle_type','origin','destination','note','from_date_time','to_date_time','driver_id',
                  'ticket_status', 'passenger_number')
"""
test def
"""
class CustomForeignKey(PrimaryKeyRelatedField):
    def get_queryset(self):
        return RequisitionTicketLog.objects.filter(vehicleId=2)


class RequisitionTicketLogDeatilSerializer(ModelSerializer):

    class Meta:
        model = RequisitionTicketLog
        fields = ('requisitionTicketLog_id', 'vehicle_id', 'vehicle_type','origin','destination','note','from_date_time','to_date_time','driver_id',
                  'ticket_status', 'passenger_number')


class RequisitionTicketLogRequestCreateSerializer(ModelSerializer):
    class Meta:
        model = RequisitionTicketLog
        fields = ('vehicle_type','origin','destination','note','from_date_time','to_date_time','passenger_number')

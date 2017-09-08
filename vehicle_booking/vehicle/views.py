from django.db import connection
from django.contrib.auth.models import User, Group
from vehicle.models import Vehicle, Driver, RequisitionTicketLog

from rest_framework import viewsets, generics, views, response
from vehicle.serializers import ( UserSerializer, GroupSerializer, VehicleSerializer, DriverSerializer, )


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ListVehicles(generics.ListCreateAPIView):
    """
    API endpoint that allows groups to be viewed or edited.

    """

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class ListDrivers(generics.ListCreateAPIView):
    """
    API endpoint that allows groups to be viewed or edited.

    """

    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class GetAvaialableVehiclesByDate(views.APIView):
    """
    get free vehicles by date range

    """

    def get(self, request, format=None, *args, **kwargs):
        '''
            Override default get
        '''
        from_date_time = self.request.GET.get("from_date_time")
        to_date_time = self.request.GET.get("to_date_time")

        cursor = connection.cursor()
        cursor.execute('''SELECT vehicle_id, vehicle_vehicle.vehicle_number, vehicle_vehicle.vehicle_type
                        FROM vehicle_vehicle
                        WHERE vehicle_id NOT IN
                        (
                        SELECT vehicle_requisitionticketlog.vehicle_id_id as vehicle_id
                        FROM vehicle_requisitionticketlog
                        WHERE
                             ticket_status = %s
                            AND (from_date_time, to_date_time) OVERLAPS (%s, %s)

                        )''',['Resolved',from_date_time,to_date_time])

        result = cursor.fetchall()

        free_vehicles = []

        for i in result:
            free_vehicle = {}
            free_vehicle['vehicle_id'] = i[0]
            free_vehicle['vehicle_number'] = i[1]
            free_vehicle['vehicle_type'] = i[2]
            free_vehicles.append(free_vehicle)

        return response.Response(free_vehicles)

class GetAvaialableDriversByDate(views.APIView):
    """
    get free drivers by date range

    """

    def get(self, request, format=None, *args, **kwargs):
        '''
            Override default get
        '''
        from_date_time = self.request.GET.get("from_date_time")
        to_date_time = self.request.GET.get("to_date_time")

        cursor = connection.cursor()
        cursor.execute('''SELECT driver_id, name, mobile
                        FROM vehicle_driver
                        WHERE driver_id NOT IN
                        (
                        SELECT vehicle_requisitionticketlog.driver_id_id as driver_id
                        FROM vehicle_requisitionticketlog
                        WHERE
                             ticket_status = %s
                            AND (from_date_time, to_date_time) OVERLAPS (%s, %s)

                        )''',['Resolved',from_date_time,to_date_time])

        result = cursor.fetchall()

        free_drivers = []

        for i in result:
            free_driver = {}
            free_driver['driver_id'] = i[0]
            free_driver['name'] = i[1]
            free_driver['mobile'] = i[2]
            free_drivers.append(free_driver)

        return response.Response(free_drivers)

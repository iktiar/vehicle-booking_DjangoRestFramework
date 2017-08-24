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
    get free vehicles by data range

    """

    def get(self, request, format=None, *args, **kwargs):
        '''
            Override default get
        '''
        cursor = connection.cursor()
        cursor.execute('''select vehicle_id, vehicle_vehicle.vehicle_number
                        from vehicle_vehicle
                        WHERE vehicle_id NOT IN
                        (
                        select vehicle_requisitionticketlog.vehicle_id_id as vehicle_id
                        from vehicle_requisitionticketlog
                        WHERE
                             ticket_status = 'Resolved'
                            AND (from_date_time, to_date_time) OVERLAPS ('2017-01-01 00:00:00+00', '2017-01-04 00:00:00')

                        )''')

        result = cursor.fetchall()

        free_vehicles = {}
        for i in result:
            free_vehicles['id'] = i[0]
            free_vehicles['number'] = i[1]

        return response.Response(free_vehicles)

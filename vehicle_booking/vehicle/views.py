
from django.contrib.auth.models import User, Group
from vehicle.models import Vehicle, Driver, RequisitionTicketLog

from rest_framework import viewsets, generics
from vehicle.serializers import ( UserSerializer, GroupSerializer, VehicleSerializer, DriverSerializer,
                                  RequisitionTicketLogSerializer, RequisitionTicketLogForAdminSerializer, )


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


class ListRequisitionTicketLogForAdmin(generics.ListCreateAPIView):
    """
    API endpoint that allows groups to be viewed or edited.

    """

    queryset = RequisitionTicketLog.objects.all()
    serializer_class = RequisitionTicketLogForAdminSerializer


class ListRequisitionTicketLogs(generics.CreateAPIView):

    queryset = RequisitionTicketLog.objects.all()
    serializer_class = RequisitionTicketLogSerializer

    def perform_create(self, serializer):
        serializer.save(submitedUser=self.request.user)

from django.db.models import Q
import datetime
from django.shortcuts import render
from vehicle.models import RequisitionTicketLog

from rest_framework import  generics, views
from requisitionticket.serializers import (
                                  RequisitionTicketLogRequestCreateSerializer,
                                  RequisitionTicketLogListSerializer,
                                  RequisitionTicketLogDeatilSerializer)


# Create your views here.
class RequisitionTicketLogUpdateView (generics.RetrieveUpdateAPIView):

    queryset = RequisitionTicketLog.objects.all()
    serializer_class = RequisitionTicketLogDeatilSerializer

    def perform_create(self, serializer):
        serializer.save(submited_user=self.request.user)


class RequisitionTicketLogListView(generics.ListCreateAPIView):

    queryset = RequisitionTicketLog.objects.all()
    serializer_class = RequisitionTicketLogListSerializer

    def get_queryset(self, *args, **kwargs):
        # queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = RequisitionTicketLog.objects.filter(submited_user__gte=0)  # filter(user=self.request.user)

        """
        queryset_list = RequisitionTicketLog.objects.all()

        query_fromDateTime = self.request.GET.get("fromDateTime")
        query_toDateTime = self.request.GET.get("toDateTime")

        queryset_list = RequisitionTicketLog.objects.filter(fromDateTime__gte=datetime.datetime(query_fromDateTime),
                                                            toDateTime__lte=datetime.datetime(query_toDateTime)
                                                            )
        """
        return queryset_list


class RequisitionTicketLogsCreateView (generics.CreateAPIView):

    queryset = RequisitionTicketLog.objects.all()
    serializer_class = RequisitionTicketLogRequestCreateSerializer

    def perform_create(self, serializer):
        serializer.save(submited_user=self.request.user)


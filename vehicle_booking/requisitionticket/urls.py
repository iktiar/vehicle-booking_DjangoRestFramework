from django.conf.urls import url

from .views import (
    RequisitionTicketLogsCreateView,
    RequisitionTicketLogListView,
    RequisitionTicketLogUpdateView
    )

urlpatterns = [
    url(r'^$', RequisitionTicketLogListView.as_view(), name='list_requisition_ticket_for_admin'),
    url(r'^create/$', RequisitionTicketLogsCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[\w-]+)/edit/$', RequisitionTicketLogUpdateView.as_view(), name='update'),
]

"""
   url(r'^admin', ListRequisitionTicketLogForAdmin.as_view(), name='list_requisition_ticket_for_admin'),
   url(r'^api/car-requisition/', RequisitionTicketLogsCreateView.as_view(), name='list_car_requisition'),
"""

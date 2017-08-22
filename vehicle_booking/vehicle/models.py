from django.db import models
from django.conf import settings
# Create your models here.


class Vehicle(models.Model):
    VEHICLE_TYPES = (
        ('Bus', 'Bus'),
        ('MicroBus', 'MicroBus'),
        ('Car', 'Car'),
    )
    VEHICLE_STATUS = (
        ('Active', 'Active'),
        ('InActive', 'InActive')
    )
    vehicleId = models.AutoField(primary_key=True)
    vehicleNumber = models.CharField(max_length=100, blank=False, unique=True)
    type = models.CharField(max_length=8, choices=VEHICLE_TYPES)
    driverId = models.ForeignKey('Driver', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=8, choices=VEHICLE_STATUS)


class Driver(models.Model):
    driverId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    mobile = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)


class RequisitionTicketLog(models.Model):
    VEHICLE_TYPES = (
        ('Bus', 'Bus'),
        ('MicroBus', 'MicroBus'),
        ('Car', 'Car'),
    )
    Submitted = 'Submitted';
    Resolved = 'Resolved';
    Rescheduled = 'Rescheduled';

    REQUISITION_TICKET_TYPES = (
        ('Submitted', Submitted),
        ('Resolved', Resolved),
        ('Rescheduled', Rescheduled),
    )
    requisitionTicketLogId = models.AutoField(primary_key=True)
    type = models.CharField(max_length=8, choices=VEHICLE_TYPES)
    origin = models.CharField(max_length=255, blank=False)
    destination = models.CharField(max_length=255, blank=False)
    driverId = models.ForeignKey('Driver', null=True)
    ticketStatus = models.CharField(max_length=10, choices=REQUISITION_TICKET_TYPES, default=Submitted)
    note = models.CharField(max_length=255, blank=True)
    fromDateTime = models.DateTimeField(blank=False)
    toDateTime = models.DateTimeField(blank=False)
    submitedUser = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)






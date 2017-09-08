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
        ('Free', 'Free'),
        ('InActive', 'InActive'),
        ('Booked','Booked')
    )
    vehicle_id = models.AutoField(primary_key=True)
    vehicle_number = models.CharField(max_length=100, blank=False, unique=True)
    vehicle_type = models.CharField(max_length=8, choices=VEHICLE_TYPES)
    driver_id = models.ForeignKey('Driver', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=8, choices=VEHICLE_STATUS)

    def __unicode__(self):
        return u'%s' % (self.vehicle_number)

    def __str__(self):
        return self.vehicle_number


class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    mobile = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.name)

    def __str__(self):
        return self.name

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
    requisitionTicketLog_id = models.AutoField(primary_key=True)
    vehicle_type = models.CharField(max_length=8, choices=VEHICLE_TYPES)
    origin = models.CharField(max_length=255, blank=False)
    destination = models.CharField(max_length=255, blank=False)
    driver_id = models.ForeignKey('Driver', null=True)
    driver_name = models.CharField(max_length=100, null=True)
    vehicle_id = models.ForeignKey('Vehicle',null=True)
    vehicle_number = models.CharField(max_length=100, null=True)
    ticket_status = models.CharField(max_length=10, choices=REQUISITION_TICKET_TYPES, default=Submitted)
    note = models.CharField(max_length=255, blank=True)
    from_date_time = models.DateTimeField(blank=False)
    to_date_time = models.DateTimeField(blank=False)
    passenger_number = models.IntegerField(blank=False)
    submited_user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.requisitionTicketLog_id


    #get all vechie in book range

    #get all vehicle - booked vechile in bookrange





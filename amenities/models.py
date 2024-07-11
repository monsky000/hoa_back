from django.db import models
from members.models import MemReg
from contractors.models import Contractors

class Amenities(models.Model):
  id=models.AutoField(primary_key = True)
  amenity_name=models.CharField(max_length=50, blank=True, null=True)
  location=models.CharField(max_length=220, blank=True, null=True)
  description=models.TextField()
  AMENITY_STATUS=[("For Approval", "For Apporval" ),("Active", "Active" ),("Inactive", "Inactive" )] 
  status=models.CharField(max_length=50, choices = AMENITY_STATUS, default="For Approval")
  is_deleted=models.BooleanField(default=False)
  create_date=models.DateTimeField(auto_now=True)
  
class Reservations(models.Model):
  id=models.AutoField(primary_key=True)
  member=models.ForeignKey(MemReg, on_delete=models.CASCADE, db_column="member_id")
  amenity=models.ForeignKey(Amenities, on_delete=models.CASCADE, db_column="amenity_id")
  sched_from=models.DateTimeField()
  sched_to=models.DateTimeField()
  RES_STATUS=[("For Approval", "For Apporval" ),("Active", "Active" ),("Inactive", "Inactive" )] 
  status=models.CharField(max_length=50, choices = RES_STATUS, default="For Approval")
  is_deleted=models.BooleanField(default=False)
  create_date=models.DateTimeField(auto_now=True)

class Maintenance(models.Model):
  id=models.AutoField(primary_key=True)
  amenity=models.ForeignKey(Amenities, on_delete=models.CASCADE, db_column="amenity_id")
  contractor=models.ForeignKey(Contractors, on_delete=models.CASCADE, db_column="contractor_id")
  sched_from=models.DateField()
  sched_to=models.DateField()
  description=models.TextField()
  maintenance_cost=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
  is_deleted=models.BooleanField(default=False)
  REPAIR_STATUS=[("Upcoming", "Upcoming" ),("Ongoing", "Ongoing" ),("Done", "Done" )] 
  status=models.CharField(max_length=50, choices = REPAIR_STATUS, default="Upcoming")
  create_date=models.DateTimeField(auto_now=True)
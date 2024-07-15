from django.db import models
from members.models import MemReg

class Positions(models.Model):
  id = models.AutoField(primary_key=True)
  position_name = models.CharField(max_length=100)
  description = models.TextField()
  is_deleted = models.BooleanField(default=False)
  create_date=models.DateTimeField(auto_now=True)

class Elections(models.Model):
  id = models.AutoField(primary_key=True)
  date = models.DateField()
  cutoff_time = models.TimeField()
  ELEC_STATUS = [('Incoming', 'Imcoming'),('Open', 'Open'),('Closed', 'Closed')]
  status = models.CharField(max_length=50, choices = ELEC_STATUS, default="Incomming")
  is_deleted = models.BooleanField(default=False)
  create_date=models.DateTimeField(auto_now=True)
  
class Nominations(models.Model):
  id=models.AutoField(primary_key=True)
  member=models.ForeignKey(MemReg, on_delete=models.CASCADE, db_column='member_id')
  election=models.ForeignKey(Elections, on_delete=models.CASCADE, db_column='election_id')
  position=models.ForeignKey(Positions, on_delete=models.CASCADE, db_column='position_id')
  is_deleted = models.BooleanField(default=False)
  create_date=models.DateTimeField(auto_now=True)
  
class Votes(models.Model):
  id=models.AutoField(primary_key=True) 
  nomination=models.ForeignKey(Nominations, on_delete=models.CASCADE, db_column='nomination_id')
  qr_code = models.ImageField(upload_to='qr_codes/', null=True, blank=True)
  is_deleted = models.BooleanField(default=False)

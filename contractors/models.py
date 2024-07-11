from django.db import models

class Contractors(models.Model):
  id=models.AutoField(primary_key = True)
  contractor_name=models.CharField(max_length=200,blank=True,null=True,unique=True)
  is_individual=models.BooleanField()
  mobile_no=models.CharField(max_length=15,blank=True,null=True,unique=True)
  landline=models.CharField(max_length=15,blank=True,null=True,unique=True)
  address=models.TextField()
  contact_person=models.CharField(max_length=200,blank=True,null=True,unique=True)
  is_deleted=models.BooleanField(default=False)
  create_date=models.DateTimeField(auto_now=True)
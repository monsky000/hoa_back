from django.db import models

class MemReg (models.Model):
  id = models.AutoField(primary_key = True)
  reg_form_no = models.CharField(max_length=50, blank=True, null=True)
  family_name = models.CharField(max_length=100, blank=True, null=True)
  first_name = models.CharField(max_length=10, blank=True, null=True)
  middle_name = models.CharField(max_length=100, blank=True, null=True)
  blk= models.IntegerField(blank=True, null=True)
  lot = models.IntegerField(blank=True, null=True)
  phase = models.IntegerField(blank=True, null=True)
  street = models.CharField(max_length=50, blank=True, null=True)
  landline = models.CharField(max_length=50, blank=True, null=True)
  mobile = models.CharField(max_length=50, blank=True, null=True)
  email = models.EmailField(max_length=50, blank=True, null=True)
  fb_name = models.CharField(max_length=50, blank=True, null=True)
  formFile = models.FileField(upload_to='member_img/', blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  REG_STATUS = [("For Approval", "FOR_APPROVAL" ),("Active", "ACTIVE" ),("Suspension", "SUSPENDED" ),("Disable", "DISABLED" )]
  EDUC_CHOICE = [("Post_Grad", "POSTGRAD" ),("College", "COLLEGE" ),("High_School", "HIGH_SCHOOL" ),("Elementary", "ELEMENTARY" )]
  reg_status = models.CharField(max_length=50, choices = REG_STATUS, default="FOR_APPROVAL")
  educ = models.CharField(max_length=50, choices = EDUC_CHOICE)
  profession = models.CharField(max_length=100, blank=True, null=True)
  is_deleted = models.BooleanField(default=False)
  create_date = models.DateTimeField(auto_now = True)
  
class Occupants(models.Model):
  id = models.AutoField(primary_key=True)
  member = models.ForeignKey(MemReg, on_delete=models.CASCADE)
  givenname = models.CharField(max_length=255)
  surname = models.CharField(max_length=255)
  age = models.IntegerField()
  relationship = models.CharField(max_length=100)
  GENDER_CHOICE = [('M', 'MALE'),('F', 'FEMALE'),]
  gender = models.CharField(max_length=50, choices = GENDER_CHOICE)
  

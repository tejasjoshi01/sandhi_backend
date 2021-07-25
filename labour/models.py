from django.db import models
import uuid


SKILL_CHOICES = (
          ("ELECTRICIAN", "ELECTRICIAN"),
          ("PLUMBER", "PLUMBER"),
          ("LABOUR", "LABOUR"),
          ("DRIVER", "DRIVER"),
          ("MAID", "MAID"),
          ("SECURITY GUARD", "SECURITY GUARD"),
          ("COOK", "COOK"),
          ("MECHANIC", "MECHANIC"),
          ("PEON", "PEON"),
          ("OTHERS", "OTHERS"),
)


LOCATION_CHOICES = (
     ("pune" , "pune") ,
     ("banglore" , "banglore") ,
     ("mumbai" , "mumbai"), 
     ("delhi" , "delhi")
)

GENDER_CHOICES = (
     ("M" , "Male") ,
     ("F" , "Female") ,
     ("O" , "Others") ,
)

class Labour(models.Model):
     first_name = models.CharField(max_length=50)
     last_name = models.CharField(max_length=50)
     age = models.IntegerField()
     gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=False)
     address_line_1 = models.CharField(max_length=255)
     address_line_2 = models.CharField(max_length=255)
     state = models.CharField(max_length=255)
     pincode = models.IntegerField()
     contact_number = models.BigIntegerField(unique=True, null=False, blank=False)
     aadhar_number = models.BigIntegerField(unique=True, null=False, blank=False)
     current_location = models.CharField(max_length=20, choices=LOCATION_CHOICES, null=False, blank=False)
     skill = models.CharField(max_length=20, choices=SKILL_CHOICES, default="OTHERS")
     message = models.TextField()



class Job(models.Model):
     employer_full_name = models.CharField(max_length=250)
     skill_required = models.CharField(max_length=20, choices=SKILL_CHOICES, default="OTHERS")
     location = models.CharField(max_length=20, choices=LOCATION_CHOICES, null=False, blank=False)
     pincode = models.IntegerField()
     employer_contact = models.BigIntegerField(unique=True, null=False, blank=False)
     message = models.TextField()









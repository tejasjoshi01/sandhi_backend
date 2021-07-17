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



class Labour(models.Model):
     first_name = models.CharField(max_length=50)
     last_name = models.CharField(max_length=50)
     age = models.IntegerField()
     address_line_1 = models.CharField(max_length=255)
     address_line_2 = models.CharField(max_length=255)
     state = models.CharField(max_length=255)
     pincode = models.IntegerField()
     contact_number = models.IntegerField(unique=True, null=False, blank=False)
     aadhar_number = models.IntegerField(unique=True, null=False, blank=False)
     date_of_birth = models.DateField()
     current_location = models.CharField(max_length=20, choices=LOCATION_CHOICES, null=False, blank=False)
     skill = models.CharField(max_length=20, choices=SKILL_CHOICES, default="OTHERS")
     message = models.TextField()



class Job(models.Model):
     employer_full_name = models.CharField(max_length=250)
     skill_required = models.CharField(max_length=20, choices=SKILL_CHOICES, default="OTHERS")
     location = models.CharField(max_length=20, choices=LOCATION_CHOICES, null=False, blank=False)
     pincode = models.IntegerField()
     employer_contact = models.IntegerField(unique=True, null=False, blank=False)
     message = models.TextField()






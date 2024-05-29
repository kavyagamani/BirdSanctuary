from django.db import models

# Create your models here.
class UserLogin(models.Model):
    username=models.CharField(max_length=60,null=True)
    password=models.CharField(max_length=40,null=True)
    utype=models.CharField(max_length=40,null=True)

class UserRegistration(models.Model):
     visitor_type=models.CharField(max_length=60,null=True)
     name=models.CharField(max_length=60,null=True)
     gender=models.CharField(max_length=60,null=True)
     city=models.CharField(max_length=60,null=True)
     address=models.CharField(max_length=60,null=True)
     email=models.CharField(max_length=60,null=True)
     mobile_no=models.CharField(max_length=10,null=True)
     id_proof=models.FileField(upload_to='documents/',null=True)

class BirdsCategory(models.Model):
     category_name=models.CharField(max_length=60,null=True)

class AddBirds(models.Model):
     category_name=models.CharField(max_length=60,null=True)
     bird_name=models.CharField(max_length=60,null=True)
     country=models.CharField(max_length=60,null=True)
     image=models.CharField(max_length=60,null=True)
     description=models.CharField(max_length=60,null=True)

class TakeAppointment(models.Model):
     visitor_type=models.CharField(max_length=60,null=True)
     user_id=models.CharField(max_length=60,null=True)
     appointment_date=models.DateField(null=True)
     appointment_timings=models.CharField(max_length=60,null=True)
     no_of_adults=models.IntegerField(null=True)
     no_of_children=models.IntegerField(null=True)
     adult_cost=models.IntegerField(null=True)
     children_cost=models.IntegerField(null=True)
     shooting_cost=models.IntegerField(null=True)
     status=models.CharField(max_length=60,null=True)
     payment_status = models.CharField(max_length=60, null=True)

class GenerateTicket(models.Model):
     appointment_id=models.IntegerField(null=True)
     ticket_no=models.IntegerField(null=True)
     user_id=models.CharField(max_length=60,null=True)
     date=models.DateField(null=True)
     time=models.CharField(max_length=100,null=True)
     amount=models.IntegerField(null=True)
     payment_date = models.DateField(null=True)
     qrcode = models.ImageField(upload_to='docs/',null=True)

class OtpCode(models.Model):
     otp=models.IntegerField()
     status=models.CharField(max_length=30)


class PriceMaster(models.Model):
     visitor_type=models.CharField(max_length=100)
     adult_cost=models.IntegerField()
     children_cost = models.IntegerField()
     

     

from django.db import models

class Customer(models.Model):
    msisdn = models.CharField(max_length=100)
    imsi = models.CharField(max_length=100)
    imei= models.CharField(max_length=100)
    plan= models.CharField(max_length=100)
    call_type= models.CharField(max_length=100)
    corresp_type= models.CharField(max_length=100)
    corresp_isdn= models.CharField(max_length=100)
    duration= models.IntegerField(max_length=100)
    date_time= models.DateTimeField(max_length=100)
    customer_name = models.CharField(max_length=1000, null= True) ## adding customer name to the database.

    

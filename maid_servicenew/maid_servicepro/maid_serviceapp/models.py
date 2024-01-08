from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=30,null=True)
    password = models.CharField(max_length=10,null=True)
    status = models.IntegerField(null=True)

    def __str__(self):
        return str(self.username)

class Customer_Register(models.Model):
    id=models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30, null=True)
    c_firstname = models.CharField(max_length=200, null=True)
    c_lastname = models.CharField(max_length=200, null=True)
    c_email = models.CharField(max_length=30,null=True)
    c_image = models.FileField(null=True)
    c_phoneno = models.IntegerField(null=True)
    c_birthdate = models.DateField(null=True)
    c_streetaddress = models.TextField(null=True)
    c_city = models.CharField(max_length=100, null=True)
    c_state = models.CharField(max_length=100, null=True)
    c_pincode = models.IntegerField(null=True)
    c_country = models.CharField(max_length=100, null=True)
    c_dbooking = models.DateField(null=True)
    request = models.CharField(max_length=15)


    def __str__(self) :
        return str(self.c_firstname)

class Serviceman_Register(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30, null=True)
    s_firstname = models.CharField(max_length=200, null=True)
    s_lastname = models.CharField(max_length=200, null=True)
    s_email = models.CharField(max_length=30,null=True)
    s_image = models.FileField(null=True)
    s_phoneno = models.IntegerField(null=True)
    s_birthdate = models.DateField(null=True)
    s_streetaddress = models.TextField(null=True)
    s_city = models.CharField(max_length=100, null=True)
    s_state = models.CharField(max_length=100, null=True)
    s_pincode = models.IntegerField(null=True)
    s_country = models.CharField(max_length=100, null=True)
    s_wexp = models.IntegerField(null=True)
    s_dapp = models.DateField(null=True)
    s_scity = models.CharField(max_length=400,null=True)
    s_typid = models.CharField(max_length=400,null=True)
    s_service = models.CharField(max_length=400,null=True)
    s_idimg = models.FileField(null=True)
    action = models.CharField(max_length=15)


    def __str__(self) :
        return str(self.s_firstname)

class Service_Category(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=100, null=True)
    image = models.FileField(null=True)
    price= models.IntegerField(null=True)

    def __str__(self):
        return self.category

class Service_City(models.Model):
    city = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.city

class Booking_Data(models.Model):
    id = models.IntegerField(primary_key=True)
    c_username = models.CharField(max_length=30, null=True)
    c_email = models.CharField(max_length=30, null=True)
    c_phoneno = models.IntegerField(null=True)
    s_servicemanname = models.CharField(max_length=200, null=True)
    s_service = models.CharField(max_length=400,null=True)
    s_scity = models.CharField(max_length=400,null=True)
    serviceman_contact = models.IntegerField(null=True)
    starting_date = models.DateField(null=True)
    ending_date = models.DateField(null=True)
    no_days = models.IntegerField(null=True)
    tot_amount = models.IntegerField(null=True)
    action = models.CharField(max_length=15)
    price_per_day= models.IntegerField(null=True)

    def __str__(self):
        return self.c_username


from django.db import models

# Create your models here.


class User(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    otp=models.IntegerField(default=123)
    is_active=models.BooleanField(default=True)
    is_verified=models.BooleanField(default=False)
    role=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True,blank=False)
    updated_at=models.DateTimeField(auto_now=True,blank=False)
    first_time_login=models.BooleanField(default=False)
    profilepic=models.FileField(upload_to="myapp/img/",default="testimonials.jpg")


class Manager(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=20)

class Company(models.Model):
    m_id=models.ForeignKey(Manager,on_delete=models.CASCADE)
    companyname=models.CharField(max_length=20,blank=True)
    companylocation=models.CharField(max_length=20,blank=True)
    companywork=models.CharField(max_length=20,blank=True)
    companycontact=models.CharField(max_length=20,blank=True)
    companylogo=models.FileField(upload_to="myapp/img/",default='default.png')

class Customer(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=20)
    billamt=models.FloatField(default=0.0)

class Products(models.Model):
    productname=models.CharField(max_length=40)
    productprice=models.IntegerField(default=000)
    productquantity=models.IntegerField(default=1)
    productimage=models.FileField(upload_to="myapp/img/")

class Reviews(models.Model):
    c_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    p_id=models.ForeignKey(Products,on_delete=models.CASCADE)
    reviewrating=models.IntegerField(default=0)
    reviewtext=models.CharField(max_length=500)


class Cart(models.Model):
    c_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    p_id=models.ForeignKey(Products,on_delete=models.CASCADE)
    product_quantity=models.IntegerField(default=1)
    product_radio = models.CharField(max_length=10)
    product_total=models.IntegerField(default=0)

class Messages(models.Model):
   message_name=models.CharField(max_length=30)
   message_email=models.CharField(max_length=50)
   message_subject=models.CharField(max_length=20)
   message=models.CharField(max_length=500)

class Subscribers(models.Model):
    email=models.EmailField(unique=True)


class Wishlist(models.Model):
    c_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    p_id=models.ForeignKey(Products,on_delete=models.CASCADE)


class Coupon(models.Model):
    couponcode=models.CharField(max_length=20)
    coupondesc=models.CharField(max_length=50)
    couponamt=models.FloatField(default=1.0)


class Billing(models.Model):
    c_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=30)
    zipcode=models.CharField(max_length=10)
    phoneno=models.CharField(max_length=10)
    comment=models.CharField(max_length=100)

class Order(models.Model):
    b_id=models.ForeignKey(Billing,on_delete=models.CASCADE)
    c_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    p_id=models.ForeignKey(Products,on_delete=models.CASCADE)
    status=models.CharField(max_length=30,default="Confirmed")
    expecteddelivery=models.DateField(null=True)
    #billamt?

from django.db import models
from django.contrib.auth.models import User
from .models import *

# admin.site.register(StudentInfo)

# Create your models here.


class StudentInfo(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    year = models.IntegerField()
    dob = models.DateField() 
    def __str__(self):
       return u'%s'%(self.name)
    
class BookInfo(models.Model):
    book_no = models.CharField(max_length=50)
    book_name = models.CharField(max_length=50)
    def __str__(self):
       return u'%s'%(self.book_name)

class Author(models.Model):
    Author_book = models.OneToOneField(BookInfo) #related_name = "jyoti")
    Author_name = models.OneToOneField(BookInfo, related_name = "rinku", null=True)
    def __str__(self):
       return u'%s'%(self.Author_name)

class Department(models.Model):
    dept_name = models.CharField(max_length=50)
    dept_id = models.IntegerField()
    def __str__(self):
       return u'%s'%(self.dept_name)

class Lib(models.Model):
    shelfno = models.IntegerField()
    book = models.ForeignKey(BookInfo)
    book_dept = models.ForeignKey(Department)
    student_name = models.OneToOneField(StudentInfo)
    def __str__(self):
       return u'%s'%(self.shelfno)



class Patient(models.Model):
    patient_id = models.IntegerField()
    patient_name = models.CharField(max_length=50)
    p_email = models.EmailField()
def __str__(self):
       return u'%s''%s'%(self.patient_id, self.patient_name)

class Doctor(models.Model):
    doct_name = models.CharField(max_length=60)
    doct_email = models.EmailField()
    doct_patient = models.ForeignKey(Patient)

def __str__(self):
       return u'%s''%s'%(self.doct_name, self.doct_patient)

class Hospital(models.Model):
    hosp_name = models.CharField(max_length=60)
    hosp_addr = models.CharField(max_length=50)
    hospdoct = models.ManyToManyField(Doctor)
    hosp_wards = models.CharField(max_length=60)
    date = models.DateField()
def __str__(self):
       return u'%s''%s''%s''%s'%(self.hospdoct, self.hosp_name, self.hosp_wards, self.hosp_addr)














class TruckInfo(models.Model):
    truck_no = models.CharField(max_length=50)
    #trukowner= models.ForeignKey(Truckowner)
    truck_load = models.CharField(max_length=50)
    truckroute = models.CharField(max_length=70)
def __str__(self):
       return u'%s''%s''%s''%s'%(self.truck_no, self.truck_load, self.truckroute) 

class Truckowner(models.Model):
    owner_name = models.CharField(max_length=60)
    truck_no = models.ManyToManyField(TruckInfo)
    contact_no = models.IntegerField()
    place = models.CharField(max_length=50)
def __str__(self):
       return u'%s''%s''%s''%s'%(self.owner_name, self.truck_no, self.contact_no, self.place)



class Trips(models.Model):
    date = models.DateField()
    time = models.TimeField()
    tripplace= models.CharField(max_length=60)
    trip_truckno = models.ForeignKey(TruckInfo)
def __str__(self):
       return u'%s''%s''%s''%s'%(self.date, self.time, self.tripplace, self.trip_truckno)


from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from .models import *

# admin.site.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):

        list_display = ("name", "roll_no", "department")
        search_fields = ('name',)
        list_filter = (("name"),)

admin.site.register(StudentInfo, StudentInfoAdmin)





class BookInfoAdmin(admin.ModelAdmin):

        list_display = ("book_no", "book_name")
        search_fields = ('book_name',)
        list_filter = (("book_name"),)
admin.site.register(BookInfo, BookInfoAdmin)


class AuthorAdmin(admin.ModelAdmin):

        list_display = ("Author_book", "Author_name")
        search_fields = ('Author_name',)
        list_filter = (("Author_name"),)
admin.site.register(Author, AuthorAdmin)


class DepartmentAdmin(admin.ModelAdmin):

        list_display = ("dept_name", "dept_id")
        search_fields = ('dept_name',)
        list_filter = (("dept_name"),)
admin.site.register(Department, DepartmentAdmin)


class LibAdmin(admin.ModelAdmin):

        list_display = ("shelfno", "book", "book_dept", "student_name")
        search_fields = ('book',)
        list_filter = (("book"),)
admin.site.register(Lib, LibAdmin)





class HospitalAdmin(admin.ModelAdmin):
        list_display = ("hosp_name","get_hospdoct", "hosp_addr", "hosp_wards")

        def get_hospdoct(self,obj):
                return "\n".join([p.doct_name for p in obj.hospdoct.all()])
        get_hospdoct.short_description = 'hospdoct1'
admin.site.register(Hospital, HospitalAdmin)
#"\n".join([Hospital.hospdoc for hospdoc in Hospital.hospdoc.all()])
#"\n".join([p.name for p in obj.hospdoc.all()])

class DoctorAdmin(admin.ModelAdmin):
        list_display = ("doct_name", "doct_email", "doct_patient")
admin.site.register(Doctor, DoctorAdmin)


class PatientAdmin(admin.ModelAdmin):
        list_display = ("patient_id", "patient_name")
        search_fields = ('patient_name',)
        list_filter = (("patient_name"),)
admin.site.register(Patient, PatientAdmin)



#class PatientAdmin(admin.ModelAdmin):

#     list_display = ("id", "get_full_name", "address", "area", "city", "franchisee", "is_active")
#     search_fields = ('name', 'description', 'keyword', )
#     list_filter = (("franchisee"),)

# admin.site.register(Patient, PatientAdmin)
#40 mins


class TruckInfoAdmin(admin.ModelAdmin):
         list_display = ("truck_no", "truckroute", "truck_load")
admin.site.register(TruckInfo, TruckInfoAdmin)

class TruckownerAdmin(admin.ModelAdmin):
        list_display = ("owner_name", "get_truck_no", "contact_no", "place")
        def get_truck_no(self,obj):
                return "\n".join([p.truck_no for p in obj.truck_no.all()])
        get_truck_no.short_description = 'trucknum'
admin.site.register(Truckowner, TruckownerAdmin)


        
class TripsAdmin(admin.ModelAdmin):
        list_display = ("date", "time", "tripplace", "trip_truckno")
admin.site.register(Trips, TripsAdmin)





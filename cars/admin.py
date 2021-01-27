from django.contrib import admin
from . models import Car

# Register your models here.
class CarAdmin(admin.ModelAdmin): #for table creation on admin panel

    list_display = ('id','car_title','color','model','year','fuel_type','is_featured')
    list_display_links = ('id','car_title')
    list_editable  = ('is_featured',)
    search_fields = ('id','car_title','city','model','fuel_type')
    list_filter = ('city','model','fuel_type')
admin.site.register(Car, CarAdmin)

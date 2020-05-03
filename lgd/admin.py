from django.contrib import admin
from .models import *

# Register your models here.
class ZilaAdmin(admin.ModelAdmin):
    list_display = ('division_geocode','zila_flid' , 'zila_geocode', 'zila_name_en', 'zila_name_bn')
    list_filter = ('division_geocode',)
    search_fields = ('zila_geocode', 'zila_name_en', 'zila_name_bn',)


admin.site.register(Zila, ZilaAdmin)

class UpazilaAdmin(admin.ModelAdmin):
    list_display = ('upazila_flid', 'upazila_geocode', 'upazila_name_en', 'upazila_name_bn')
    # list_filter = ('zila_geocode',)
    search_fields = ('upazila_geocode', 'upazila_name_en', 'upazila_name_bn',)


admin.site.register(Upazila, UpazilaAdmin)

# class UnionAdmin(admin.ModelAdmin):
#     list_display = ('upazila_geocode', 'union_geocode', 'union_name_en', 'union_name_bn')
#     list_filter = ('upazila_geocode',)
#     search_fields = ('union_geocode', 'union_name_en', 'union_name_bn',)


# admin.site.register(Union, UnionAdmin)
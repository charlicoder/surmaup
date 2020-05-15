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
    list_filter = ('zila',)
    search_fields = ('upazila_geocode', 'upazila_name_en', 'upazila_name_bn',)

admin.site.register(Upazila, UpazilaAdmin)


class UnionAdmin(admin.ModelAdmin):
    list_display = ('union_name_bn', 'union_geocode', 'total_mouja', 'total_villages', 'total_area')
    list_filter = ('upazila',)
    search_fields = ('union_flid', 'union_name_en', 'union_name_bn',)

admin.site.register(Union, UnionAdmin)


class MoujaAdmin(admin.ModelAdmin):
    list_display = ('mouja_name_bn', 'mouja_geocode', 'jl_no', 'total_area_of_land')
    list_filter = ('union',)
    search_fields = ('mouja_flid',)

admin.site.register(Mouja, MoujaAdmin)


class VillageAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "moujav":
            # import pdb ; pdb.set_trace()
            kwargs["queryset"] = Mouja.objects.filter(union='6090033711')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ('village_name_bn', 'moujav', 'union')
    list_filter = ('union', 'moujav',)
    search_fields = ('village_flid', 'village_name_en', 'village_name_bn')

admin.site.register(Village, VillageAdmin)
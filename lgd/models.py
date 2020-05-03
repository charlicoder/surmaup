from django.db import models
from django.db.models import Max
from random import randint

# Create your models here.
class Zila(models.Model):
    zila_flid = models.CharField(primary_key=True, editable=False, max_length=4, default=randint(0,1000))
    zila_geocode = models.CharField(max_length=2, null=False, blank=False)
    division_geocode = models.CharField(max_length=2, null=False, blank=False)
    zila_name_en = models.CharField(max_length=30, null=True, blank=True)
    zila_name_bn = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.zila_flid
    
    def save(self, **kwargs):
        if not self.zila_flid:
            self.zila_flid = self.division_geocode + self.zila_geocode
        super().save(*kwargs)



class Upazila(models.Model):
    zila = models.ForeignKey(Zila, null=False, blank=False, on_delete=models.CASCADE)
    upazila_flid = models.CharField(primary_key=True, editable=False, max_length=6, default=randint(0,1000))
    # zila_geocode = models.CharField(max_length=2, null=False, blank=False)
    # division_geocode = models.CharField(max_length=2, null=False, blank=False)
    upazila_geocode = models.CharField(max_length=2, null=False, blank=False)
    upazila_name_en = models.CharField(max_length=30, null=True, blank=True)
    upazila_name_bn = models.CharField(max_length=30, null=True, blank=True)
    
    

    def __str__(self):
        return self.upazila_flid
    
    def save(self, **kwargs):
        if not self.upazila_flid:
            self.upazila_flid = self.zila.zila_flid + self.upazila_geocode
        super().save(*kwargs)


# class Union(models.Model):
#     union_geocode = models.CharField(max_length=5, null=False, blank=False)
#     union_geocode_old = models.CharField(max_length=5, null=True, blank=True)
#     union_name_en = models.CharField(max_length=30, null=True, blank=True)
#     union_name_bn = models.CharField(max_length=30, null=True, blank=True)
#     upazila_geocode = models.CharField(max_length=3, null=True, blank=True)
#     upazila = models.ForeignKey(Upazila, null=True, blank=True, on_delete=models.SET_NULL)
    

#     def __str__(self):
#         return self.union_geocode


# class Village(models.Model):
#     village_name_en = models.CharField(max_length=30, null=False, blank=False)
#     village_name_bn = models.CharField(max_length=30, null=True, blank=True)
#     union_geocode = models.CharField(max_length=5, null=False, blank=False)
#     union = models.ForeignKey(Union, null=True, blank=True, on_delete=models.SET_NULL)
#     upazila_geocode = models.CharField(max_length=3, null=True, blank=True)
#     upazila = models.ForeignKey(Upazila, null=True, blank=True, on_delete=models.SET_NULL)
#     village_code = models.CharField(max_length=4, null=True, blank=True)
#     mouja_code = models.CharField(max_length=4, null=True, blank=True)

#     class Meta:
#         unique_together = ('village_code', 'mouja_code',)

#     def __str__(self):
#         return self.village_name_en


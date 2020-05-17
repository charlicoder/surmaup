from django.db import models
from django.db.models import Max
from random import randint
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Zila(models.Model):
    zila_flid = models.CharField(primary_key=True, editable=False, max_length=4)
    zila_geocode = models.CharField(max_length=2, null=False, blank=False)
    division_geocode = models.CharField(max_length=2, null=False, blank=False)
    zila_name_en = models.CharField(max_length=30, null=True, blank=True)
    zila_name_bn = models.CharField(max_length=30, null=True, blank=True)


    def clean(self):
        if self.division_geocode is None:
            raise ValidationError({'division_geocode': _('Division Geocode is a required field!')})

    def __str__(self):
        return self.zila_name_bn
    
    def save(self, **kwargs):
        if not self.zila_flid:
            self.zila_flid = self.division_geocode + self.zila_geocode
        super().save(*kwargs)
    
    @property
    def division_flid(self):
        return self.division_geocode



class Upazila(models.Model):
    zila = models.ForeignKey(Zila, null=False, blank=False, on_delete=models.CASCADE)
    upazila_flid = models.CharField(primary_key=True, editable=False, max_length=7)

    # With present geocode max_length 2 is enough but will propose for 3
    upazila_geocode = models.CharField(max_length=3, null=False, blank=False)

    upazila_name_en = models.CharField(max_length=30, null=True, blank=True)
    upazila_name_bn = models.CharField(max_length=30, null=True, blank=True)


    def __str__(self):
        return self.upazila_name_en
    
    def save(self, **kwargs):
        if not self.upazila_flid:
            self.upazila_flid = self.zila.zila_flid + self.upazila_geocode
        super().save(*kwargs)
    
    @property
    def zila_flid(self):
        return self.zila.zila_flid
    
    @property
    def division_flid(self):
        return self.zila.division_flid
    
    @property
    def zila_name_en(self):
        return self.zila.zila_name_en
    
    @property
    def zila_name_bn(self):
        return self.zila.zila_name_bn




class Union(models.Model):
    upazila = models.ForeignKey(Upazila, null=False, blank=False, on_delete=models.CASCADE)
    union_flid = models.CharField(primary_key=True, editable=False, max_length=11)
    union_geocode = models.CharField(max_length=4, null=False, blank=False)
    union_geocode_old = models.CharField(max_length=2, null=True, blank=True)
    union_name_en = models.CharField(max_length=30, null=True, blank=True, verbose_name=_('union name (En)'),)
    union_name_bn = models.CharField(max_length=30, null=True, blank=True, verbose_name=_('union name (Bn)'),)
    

    def __str__(self):
        return self.union_name_en
    
    def __unicode__(self):
        return self.union_name_en
    
    def save(self, **kwargs):
        if not self.union_flid:
            self.union_flid = self.upazila.upazila_flid + self.union_geocode
        super().save(*kwargs)
    
    
    @property
    def division_flid(self):
        return self.upazila.division_flid
    
    @property
    def total_area(self):
        moujas = Mouja.objects.filter(union=self)
        area = 0
        for m in moujas:
            area += m.total_area_of_land
        return area

    @property
    def total_mouja(self):
        moujas = Mouja.objects.filter(union=self).count()
        return moujas
    
    @property
    def total_villages(self):
        villages = Village.objects.filter(union=self).count()
        return villages
    
    @property
    def zila_flid(self):
        return self.upazila.zila_flid
    
    @property
    def zila_name_en(self):
        return self.upazila.zila_name_en
    
    @property
    def zila_name_bn(self):
        return self.upazila.zila_name_bn
    
    @property
    def upazila_flid(self):
        return self.upazila.upazila_flid
    
    @property
    def upazila_name_en(self):
        return self.upazila.upazila_name_en
    
    @property
    def upazila_name_bn(self):
        return self.upazila.upazila_name_bn
    
    # @property
    # def union_flid(self):
    #     return self.union_flid
    
    # @property
    # def union_name_en(self):
    #     return self.union_name_en
    
    # @property
    # def union_name_bn(self):
    #     return self.union_name_bn
    
    # @property
    # def union_geocode(self):
    #     return self.union_geocode
    
    # @property
    # def union_geocode_old(self):
    #     return self.union_geocode_old


class Mouja(models.Model):
    union = models.ForeignKey(Union, null=False, blank=False, on_delete=models.CASCADE)
    mouja_flid = models.CharField(primary_key=True, editable=False, max_length=14)

    jl_no = models.CharField(max_length=3, null=True, blank=True)
    mouja_geocode = models.CharField(max_length=3, null=False, blank=False)
    mouja_geocode_old = models.CharField(max_length=3, null=True, blank=True)

    mouja_name_en = models.CharField(max_length=30, null=True, blank=True)
    mouja_name_bn = models.CharField(max_length=30, null=True, blank=True)

    total_area_of_land = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    
    

    # class Meta:
    #     unique_together = ('village_code', 'mouja_code',)

    def __str__(self):
        return self.mouja_name_bn
    
    def save(self, **kwargs):
        if not self.mouja_flid:
            self.mouja_flid = self.union.union_flid + self.mouja_geocode
        super().save(*kwargs)


class Village(models.Model):
    union = models.ForeignKey(Union, null=False, blank=False, on_delete=models.CASCADE)
    moujav = models.ForeignKey(Mouja, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Mouja')

    village_flid = models.CharField(primary_key=True, editable=False, max_length=17)
    village_geocode = models.CharField(max_length=3, null=False, blank=False)
    village_geocode_old = models.CharField(max_length=3, null=False, blank=False)

    village_name_en = models.CharField(max_length=30, null=False, blank=False)
    village_name_bn = models.CharField(max_length=30, null=True, blank=True)
    
    

    # class Meta:
    #     unique_together = ('village_code', 'mouja_code',)

    def __str__(self):
        return self.village_name_en
    
    def __unicode__(self):
        return self.village_name_en
    
    def save(self, **kwargs):
        if not self.village_flid:
            self.village_flid = self.moujav.mouja_flid + self.village_geocode
        super().save(*kwargs)
    
    @property
    def division_flid(self):
        return self.union.division_flid

    @property
    def zila_flid(self):
        return self.union.zila_flid
    
    @property
    def zila_name_en(self):
        return self.union.zila_name_en
    
    @property
    def zila_name_bn(self):
        return self.union.zila_name_bn
    
    @property
    def upazila_flid(self):
        return self.union.upazila_flid
    
    @property
    def upazila_name_en(self):
        return self.union.upazila_name_en
    
    @property
    def upazila_name_bn(self):
        return self.union.upazila_name_bn
    
    @property
    def union_flid(self):
        return self.union.union_flid
    
    @property
    def union_name_en(self):
        return self.union.union_name_en
    
    @property
    def union_name_bn(self):
        return self.union.union_name_bn
    
    @property
    def mouja(self):
        return self.moujav.mouja_geocode
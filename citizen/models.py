# from django.db import models
# from lgd.models import Village
# # Create your models here.

# class Citizen(models.Model):
#     SEX = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('B', 'Both')
#     )

#     RELEGION = (
#         ('M', 'Islam'),
#         ('H', 'Hindu'),
#         ('C', 'Christian')
#     )
#     village = models.ForeignKey(Village, null=False, blank=False, on_delete=models.SET_NULL)
#     # citizen_id = models.CharField(max_length=30, blank=True, null=True)
#     citizen_nid = models.CharField(max_length=18, null=True, blank=True, unique=True)
#     citizen_brn = models.CharField(max_length=18, null=True, blank=True, unique=True)
#     name_en = models.CharField(max_length=30, blank=True, null=True)
#     name_bn = models.CharField(max_length=30, blank=True, null=True)
#     father_name = models.CharField(max_length=30, blank=True, null=True)
#     mother_name = models.CharField(max_length=30, blank=True, null=True)
#     spouse_name = models.CharField(max_length=30, blank=True, null=True)
#     dob = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
#     religion = models.CharField(max_length=2, choices=RELEGION, null=True, blank=True)
#     gender = models.CharField(max_length=2, choices=SEX, null=True, blank=True)

#     class Meta:
#         verbose_name = 'Citizen'
#         verbose_name_plural = 'Citizens'
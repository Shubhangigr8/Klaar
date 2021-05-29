from django.db import models

# Create your models here.
class Branches(models.Model):
    id = models.AutoField(primary_key=True)
    ifsc = models.CharField(max_length=150)
    bank_id = models.IntegerField()
    branch = models.CharField(max_length=150)
    bank_id = models.CharField(max_length=150)
    address = models.TextField()
    city = models.CharField(max_length=150)
    district = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    bank_name = models.CharField(max_length=150)
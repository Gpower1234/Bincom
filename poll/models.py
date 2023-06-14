from django.db import models

# Create your models here.

class pollingUnitResult(models.Model):
    result_id = models.IntegerField(null=False)
    polling_unit_uniqueid = models.IntegerField(null=False)
    party_abbreviation = models.CharField(max_length=4, null=False)
    party_score = models.IntegerField(null=False)
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateTimeField(null=False)
    user_ip_address = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.party_abbreviation

class WardResult(models.Model):
    ward_id = models.IntegerField(null=False)
    ward_name = models.CharField(max_length=50, null=False)
    total_votes = models.IntegerField()
    lga_id = models.IntegerField(null=False)
    ward_description = models.TextField()
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateTimeField(null=False)
    user_ip_address = models.CharField(max_length=50, null=False)
    

    def __str__(self):
        return self.ward_name





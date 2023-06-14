from django import forms
from .models import pollingUnitResult

class WardResultForm(forms.ModelForm):
    class Meta:
        model = pollingUnitResult
        fields = ['result_id', 'polling_unit_uniqueid', 'party_abbreviation', 'entered_by_user', 'date_entered', 'user_ip_address']
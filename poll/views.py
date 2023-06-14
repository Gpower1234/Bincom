from django.shortcuts import render
from .models import *
# Create your views here.

def Home(request):
    return render(request, 'home.html')

def PollingUnitResult(request):
    polling_unit_result = pollingUnitResult.objects.all() 
    return render(request, 'pollingUnitResult.html', {'polling_unit_result': polling_unit_result })

def wardResult(request):
    ward_result = WardResult.objects.all()
    return render(request, 'wardResult.html', {'ward_result': ward_result})

def AddPollinUnitResult(request):
    if request.method == 'POST':
        addPollinUnitResult = pollingUnitResult.objects.get_or_create(
            ward_id = ward_id,
            ward_name = ward_name,
            total_votes = total_votes,
            lga_id = LGA,
            ward_description = description,
            entered_by_user = entered_by,
            date_entered = date_entered,
            user_ip_address = user_ip_address
    )
    return render(request, 'addPollingUnitResult.html')
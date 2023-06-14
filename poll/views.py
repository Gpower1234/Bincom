from django.shortcuts import render, redirect
from .models import *
from .forms import WardResultForm

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
        form = WardResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            return redirect('failed')
    else: 
        form = WardResultForm()

    context = {'form': form}

    return render(request, 'addPollingUnitResult.html', context)

def Success(request):
    return render(request, 'success.html')
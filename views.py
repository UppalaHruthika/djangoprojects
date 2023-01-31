from django.shortcuts import render
from django.views.generic import TemplateView



def home(request):
    return render(request,'Main.html')
# Create your views here.
def contact_us(request):
    return render(request,'contactus.html')
def gallery(request):
    return render(request,'gallery.html')
    
def rates(request):
    return render(request,'rates.html')
def our_facility(request):
    return render(request,'ourfacility.html')

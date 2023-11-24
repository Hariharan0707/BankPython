from django.shortcuts import render
from .models import Place, District, Branch, Service
from django.http.response import HttpResponse, JsonResponse
from django.core import serializers
import json
# Create your views here.
def index(request):
    obj=Place.objects.all()
    return render(request,'index.html',{'result':obj})





# Create your views here.

def getdata(request):
    template_name = 'form.html'
    discontext = District.objects.all()
    brancontext = Branch.objects.all()

    return render(request, template_name, {'district': discontext, 'branch': brancontext})

def final(request):
    return render(request,'final.html')

def new(request):
    service=Service.objects.all()
    context={
        'service_list':service
    }
    return render(request,'new.html',context)
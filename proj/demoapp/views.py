from django.shortcuts import render
from django.http import HttpResponse
from .tasks import mul

def index(request):
    result = mul(2,3)
    
    return HttpResponse("The result of a great computation of the multiplication of 2 and 3 is {0}".format(result))
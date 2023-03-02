from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'mycart/design.html')

def index(request):
    return HttpResponse('Congaratulations you have created an webb app using Django')

def facebook(request):
    return render(request,'mycart/facebook.html')

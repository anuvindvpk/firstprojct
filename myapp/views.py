from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'homepage/baabtrahome.html')

def about(request):
    return render(request,'homepage/about.html')

def contact(request):
    return render(request,'homepage/contact.html')

def viewpage(request):
    return render(request,'homepage/viewpage.html')

    
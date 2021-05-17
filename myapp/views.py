from django.shortcuts import render
from django.conf import settings
from .models import Contact

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about-us.html')

def service(request):
    return render(request,'services.html')

def portfolio(request):
    return render(request,'portfolio.html')

def blog(request):
    return render(request,'blog.html')

def single_blog(request):
    return render(request,'single-blog.html')

def contact(request):
    if request.method=="POST":
        Contact.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                subject=request.POST['subject'],
                message=request.POST['message'],
            )
        msg="Contact Saved Succesfully. Will Reach You Very Soon."
        return render(request,'contact.html',{'msg':msg}) 
    else:
        return render(request,'contact.html')

def element(request):
    return render(request,'elements.html')
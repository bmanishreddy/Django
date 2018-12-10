from django.shortcuts import render


def index(request):
    return render(request ,'personal/home.html')

# Create your views here.
def contact(request):
    return render(request,'personal/basic.html',{'contact':['Here is my basic contact infor plese feel free to contact me ','bmanishreddy@gmail.com']})
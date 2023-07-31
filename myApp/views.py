from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    name = 'Rebecca'
    context = {
        'name' : name
    }
    return render(request,'myApp/index.html', context) #render method combines parameters, context can be accessed in template
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    if (request.method == 'POST'):
        print(request.FILES['file']) #check for any files posted, incl input id
    else:
        print('GET request')
    return render(request,'myApp/index.html') #render method combines parameters, context can be accessed in template
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    if (request.method == 'POST'):
        name = request.POST.get('name')
        print(name)
    else:
        print('GET request')
    return render(request,'myApp/index.html') #render method combines parameters, context can be accessed in template
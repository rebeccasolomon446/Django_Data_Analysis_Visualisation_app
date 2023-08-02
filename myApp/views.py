from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
# Create your views here.
def hello(request):
    if (request.method == 'POST'):
       file = request.FILES['file'] 
       print(pd.read_csv(file))
    else:
        print('GET request')
    return render(request,'myApp/index.html') #render method combines parameters, context can be accessed in template
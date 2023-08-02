from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from pandas.io import json
from .models import Data
# Create your views here.
def hello(request):
    if (request.method == 'POST'):
       file = request.FILES['file'] 
       df = pd.read_csv(file)
       json_data = df.reset_index().to_json(orient='records')
       data = []
       data = json.loads(json_data)
       for d in data:
        name = d['property_name']
        price = d['property_price']
        rent = d['property_rent']
        emi = d['emi']
        tax = d['tax']
        exp = d['other_exp']
        dt = Data(name=name, price=price, rent=rent, emi=emi,tax=tax, exp=exp)
        dt.save()
    else:
        print('GET request')
    return render(request,'myApp/index.html') #render method combines parameters, context can be accessed in template
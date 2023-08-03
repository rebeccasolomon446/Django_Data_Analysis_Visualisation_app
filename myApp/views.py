from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from pandas.io import json
from .models import Data

# Create your views here.
def hello(request):
    if (request.method == 'POST'):
        prev_data = Data.objects.all()
        prev_data.delete()
        # setting the uploaded file to variable file
        file = request.FILES['file'] 
        # read the uploaded file using pandas read function, set it to 'df' variable
        df = pd.read_csv(file)
        # restructure the data so that each row is its own object, set equal to 'json_data' variable
        json_data = df.reset_index().to_json(orient='records')
        data = []
        # parse json data to a python dictionary, set equal to variable 'data'
        data = json.loads(json_data)
        # loop through data set variable names to the corresponsing data column title
        for d in data:
            name = d['property_name']
            price = d['property_price']
            rent = d['property_rent']
            emi = d['emi']
            tax = d['tax']
            exp = d['other_exp']
            expenses_monthly = emi+tax+exp
            income_monthly = rent-expenses_monthly
            # creating data model that assigns each property in the Data model class to its corresponding value, set equal to variable 'dt'
            dt = Data(name=name, price=price, rent=rent, emi=emi,tax=tax, exp=exp, expenses_monthly=expenses_monthly, income_monthly=income_monthly)
            # save data to database
            dt.save()
        
        # retrieve all data
        data_objects = Data.objects.all()
        # create context to watch for changes in the data
        context = {'data_objects' : data_objects}
        # render the context taking into account the html file
        return render(request,'myApp/index.html', context)
    else:
        print('GET request')
    return render(request,'myApp/index.html') #render method combines parameters, context can be accessed in template
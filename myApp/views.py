from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from pandas.io import json
# Create your views here.
def hello(request):
    if (request.method == 'POST'):
       file = request.FILES['file'] 
       df = pd.read_csv(file)
       json_data = df.reset_index().to_json(orient='records')
       data = []
       data = json.loads(json_data)
       print(data)
    else:
        print('GET request')
    return render(request,'myApp/index.html') #render method combines parameters, context can be accessed in template
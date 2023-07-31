from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    name = 'Rebecca'
    marvel_characters = {'ironman', 'thor', 'black widow'}
    context = {
        'marvel_characters' : marvel_characters
    }
    return render(request,'myApp/index.html', context) #render method combines parameters, context can be accessed in template
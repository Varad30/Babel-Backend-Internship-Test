from urllib import response
from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    response=requests.get('https://the-one-api.dev/v2/book').json()
    search=response['docs']
    return render(request,'base.html',{'response':search})

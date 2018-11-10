from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Views are the front facing HTML that users see

def index(request):
    return HttpResponse("Imagely Index")
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def django(request):
    return HttpResponse('django is teaching by harshad sir')
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World,")
def test(request):
    return HttpResponse("Hello test,")

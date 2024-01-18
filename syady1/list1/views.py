from django.http import HttpResponse
from django.shortcuts import render


def index(request):  # HttpRequest
    return HttpResponse('listiga xush kelibsiz.')

def category(request):
    return HttpResponse("<h1>list2ga xush kelibiz.</h1>")
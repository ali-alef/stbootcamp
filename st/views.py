from django.http import HttpResponse
from django.shortcuts import render


def apply(request):
    return HttpResponse("hello")

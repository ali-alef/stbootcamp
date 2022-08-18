from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def apply(request):
    userType = request.POST['userType']
    price = request.POST['price']


def applyAction(rule, price):
    f = rule.action.fixedDisplacementAmount
    p = rule.action.percentageDisplacementAmount
    m = rule.action.maximumDisplacementAmount

    if rule.type

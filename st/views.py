from django.shortcuts import render
from .fuctions import checkRules


def apply(request):
    userType = request.POST['userType']
    price = request.POST['price']
    appliedRules = []

    checkRules(userType, price, appliedRules)



from django.http import JsonResponse
from django.shortcuts import render
from .fuctions import checkRules


def apply(request):
    if request.method == 'POST':
        userType = request.POST['userType']
        price = request.POST['price']
        appliedRules = []

        checkRules(price, appliedRules, userType)

        return JsonResponse({"appliedRules": appliedRules})

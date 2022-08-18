from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .fuctions import checkRules


@csrf_exempt
def apply(request):
    if request.method == 'POST':
        price = float(request.POST['price'])
        appliedRules = []
        checkRules(price, appliedRules, request.POST.dict())

        return JsonResponse({"appliedRules": appliedRules})


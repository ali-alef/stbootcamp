from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .fuctions import checkRules
import json

@csrf_exempt
def apply(request):
    if request.method == 'POST':
        body = request.body.decode('utf-8')
        data = json.loads(body)
        price = data['price']
        
        
        # checking for invalid inputs
        if not isinstance(price, float) or price < 0:
            print('invalid value for price')
            return JsonResponse({"applied": False,
                                 "appliedRules": []})
        
        appliedRules = []
        checkRules(price, appliedRules, data)
        applied = bool(len(appliedRules))
        return JsonResponse({"applied": applied,
                             "appliedRules": appliedRules})


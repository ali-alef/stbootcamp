from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .fuctions import checkRules


@csrf_exempt
def apply(request):
    if request.method == 'POST':
        body = request.body.decode('utf-8')
        data = json.loads(body)
        price = data['price']
        
        appliedRules = []
        checkRules(price, appliedRules, data)

        return JsonResponse({"appliedRules": appliedRules})


from .models import *


# applies the discount or markup
# returns amount of displacement and new price
def applyAction(rule, price):
    f = float(rule.action.fixedDisplacementAmount)
    p = float(rule.action.percentageDisplacementAmount)
    m = float(rule.action.maximumDisplacementAmount)
    if rule.type == "MARKUP":
        displacement = min(f + (price * p) / 100, m)
        newPrice = price + displacement
    else:
        displacement = min(f + (price * p) / 100, m)
        newPrice = price - displacement

    return displacement, newPrice


def checkRules(price, appliedRules, kwargs):
    sequence = 1

    for rule in Rule.objects.all():
        if ruleCondition(rule, kwargs):
            displacement, newPrice = applyAction(rule, price)
            dict = {
                "id": rule.id,
                "name": rule.name,
                "oldPrice": price,
                "newPrice": newPrice,
                "displacement": displacement,
                "sequence": sequence
            }

            sequence += 1

            appliedRules.append(dict)

            price = newPrice


def ruleCondition(rule, kwargs):
    for condition in rule.condition_set.all():
        if not condition.check_condition(kwargs):
            return False

    return True

from .models import *


def applyAction(rule, price):
    f = rule.action.fixedDisplacementAmount
    p = rule.action.percentageDisplacementAmount
    m = rule.action.maximumDisplacementAmount

    if rule.type == "MARKUP":
        displacement = min(f + (price * p) / 100, m)
        newPrice = price + displacement
    else:
        displacement = min(f + (price * p) / 100, m)
        newPrice = price - displacement

    return displacement, newPrice


def checkRules(price, appliedRules, userType):
    sequence = 1

    for rule in Rule.objects.all():
        if ruleCondition(rule, userType):
            displacement, newPrice = applyAction(rule, price)
            dict = {
                "rule": rule,
                "oldPrice": price,
                "newPrice": newPrice,
                "displacement": displacement,
                "sequence": sequence
            }

            sequence += 1

            appliedRules.append(dict)


def ruleCondition(rule, userType):
    pass

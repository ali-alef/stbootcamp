from django.db import models


def userType(value, kwargs):
    user_type = kwargs['userType']
    if user_type == value:
        return True

    return False


def minimumPrice(minPrice, kwargs):
    minimum_price = int(minPrice)
    price = int(kwargs['price'])

    if price > minimum_price:
        return True

    return False


funcNameDict = {"userType": userType, "minimumPrice": minimumPrice}


class funcName(models.TextChoices):
    userType = "userType"
    minimumPrice = "minimumPrice"


class Action(models.Model):
    fixedDisplacementAmount = models.DecimalField(max_digits=20, decimal_places=2)
    percentageDisplacementAmount = models.DecimalField(max_digits=10, decimal_places=2)
    maximumDisplacementAmount = models.DecimalField(max_digits=10, decimal_places=2)


class ruleType(models.TextChoices):
    MARKUP = 'MARKUP'
    DISCOUNT = 'DISCOUNT'


class Rule(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=ruleType.choices)
    action = models.OneToOneField(Action, on_delete=models.CASCADE)
    listConditions = []

    def __str__(self):
        return self.name


class Condition(models.Model):
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=200, choices=funcName.choices)
    value = models.CharField(max_length=200, null=True)

    def check_condition(self, kwargs):
        func = funcNameDict[self.type]
        return func(self.value, kwargs)

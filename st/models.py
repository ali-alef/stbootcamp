from django.db import models
from django.core.validators import MinValueValidator


class Action(models.Model):
    fixedDisplacementAmount = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0)])
    percentageDisplacementAmount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    maximumDisplacementAmount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])


class Rule(models.Model):
    
    class RuleType(models.TextChoices):
        MARKUP = 'MARKUP'
        DISCOUNT = 'DISCOUNT'

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=RuleType.choices)
    action = models.OneToOneField(Action, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Condition(models.Model):
    
    # you have to add your condition functions name here
    class ConditionFunctions(models.TextChoices):
        userType = "userType"
        minimumPrice = "minimumPrice"

    rule = models.ForeignKey(Rule, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=200, choices=ConditionFunctions.choices)
    value = models.CharField(max_length=200, null=True)

    def check_condition(self, kwargs):
        func = condition_functions[self.type]
        return func(self.value, kwargs)


# condition functions (write your condition functions here)
# -------------------------------------------------------
def userType(value, kwargs):
    user_type = kwargs['userType']
    if user_type == value:
        return True
    return False


def minimumPrice(minPrice, kwargs):
    try:
        minimum_price = float(minPrice)
        price = float(kwargs['price'])

        if price > minimum_price:
            return True
    except ValueError:
        print('invalid value for minimum price')
    return False


# you have to add your condition functions name here
condition_functions = {"userType": userType, "minimumPrice": minimumPrice}

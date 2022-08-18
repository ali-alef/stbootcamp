from django.db import models


def B2B(kwargs):
    userType = kwargs['userType']
    if userType == "B2B":
        return True
    return False


def B2C(kwargs):
    userType = kwargs['userType']
    if userType == "B2C":
        return True
    return False


funcNameDict = {"B2B": B2B, "B2C": B2C}


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


class funcName(models.TextChoices):
    B2B = 'B2B'
    B2C = 'B2C'


class Condition(models.Model):
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE, null=True)
    func_name = models.CharField(max_length=25, choices=funcName.choices)

    def check_condition(self, kwargs):
        func = funcNameDict[self.func_name]
        return func(kwargs)

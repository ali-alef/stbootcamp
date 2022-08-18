from django.db import models


class Action(models.Model):
    fixedDisplacementAmount = models.DecimalField(max_digits=20, decimal_places=2)
    percentageDisplacementAmount = models.DecimalField(max_digits=10, decimal_places=2)
    maximumDisplacementAmount = models.DecimalField(max_digits=10, decimal_places=2)


class Rule(models.Model):
    ruleChoices = [
        ('1', "DISCOUNT"),
        ('2', "MARKUP"),
    ]

    userTypeConditions = [
        ('1', "B2B"),
        ('2', "B2C"),
    ]

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=1, choices=ruleChoices)
    userTypeCondition = models.CharField(max_length=1, choices=userTypeConditions)
    action = models.OneToOneField(Action, on_delete=models.CASCADE)

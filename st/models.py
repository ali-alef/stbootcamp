from django.db import models


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

    def __str__(self):
        return self.name


class userType(models.TextChoices):
    B2B = 'B2B'
    B2C = 'B2C'


class Condition(models.Model):
    rule = models.OneToOneField(Rule, on_delete=models.CASCADE)
    userTypeCondition = models.CharField(max_length=20, choices=userType.choices)

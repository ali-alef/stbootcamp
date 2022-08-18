from django.contrib import admin
from .models import *


class RuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type')

class ConditionAdmin(admin.ModelAdmin):
    list_display = ('id', 'rule', 'type', 'value')

class ActionAdmin(admin.ModelAdmin):
    list_display = ('id', 'fixedDisplacementAmount', 'percentageDisplacementAmount', 'maximumDisplacementAmount')


admin.site.register(Rule, RuleAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(Condition, ConditionAdmin)

# Generated by Django 4.0.3 on 2022-08-18 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('st', '0003_remove_rule_usertypecondition_alter_rule_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='userTypeCondition',
            field=models.CharField(choices=[('B2B', 'B2B'), ('B2C', 'B2C')], max_length=10),
        ),
    ]

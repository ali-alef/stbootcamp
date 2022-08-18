# Generated by Django 4.0.3 on 2022-08-18 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('st', '0004_alter_condition_usertypecondition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='userTypeCondition',
            field=models.CharField(choices=[('B2B', 'B2B'), ('B2C', 'B2C')], max_length=20),
        ),
        migrations.AlterField(
            model_name='rule',
            name='type',
            field=models.CharField(choices=[('MARKUP', 'Markup'), ('DISCOUNT', 'Discount')], max_length=20),
        ),
    ]

# Generated by Django 4.0.3 on 2022-08-18 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('st', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rule',
            old_name='conditions',
            new_name='userTypeCondition',
        ),
    ]

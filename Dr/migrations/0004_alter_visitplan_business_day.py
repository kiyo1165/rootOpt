# Generated by Django 4.1 on 2023-05-14 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dr', '0003_rename_dr_id_visitplan_dr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitplan',
            name='business_day',
            field=models.IntegerField(),
        ),
    ]

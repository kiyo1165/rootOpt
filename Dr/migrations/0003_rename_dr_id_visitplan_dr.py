# Generated by Django 4.1 on 2023-05-13 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dr', '0002_visitplan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitplan',
            old_name='dr_id',
            new_name='dr',
        ),
    ]

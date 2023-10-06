# Generated by Django 3.2.7 on 2023-10-06 06:25

import Hospitals.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospitals', '0012_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.BigIntegerField(default=0, validators=[Hospitals.models.validate_rating]),
        ),
    ]

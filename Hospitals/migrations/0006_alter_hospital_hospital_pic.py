# Generated by Django 3.2.7 on 2023-10-04 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospitals', '0005_hospital_hospital_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='hospital_pic',
            field=models.ImageField(blank=True, default='profile_pic/HospitalPic/red_cross.jpg', null=True, upload_to='profile_pic/HospitalPic/'),
        ),
    ]

# Generated by Django 4.0.5 on 2022-08-02 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_personelpresenceabsence_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personelpresenceabsence',
            name='vorod',
            field=models.TimeField(verbose_name='ساعت ورود'),
        ),
    ]

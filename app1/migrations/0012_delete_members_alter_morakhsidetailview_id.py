# Generated by Django 4.0.5 on 2022-08-09 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_members'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Members',
        ),
        migrations.AlterField(
            model_name='morakhsidetailview',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

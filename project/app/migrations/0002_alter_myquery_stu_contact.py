# Generated by Django 5.1.1 on 2024-10-17 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myquery',
            name='stu_contact',
            field=models.IntegerField(null=True),
        ),
    ]

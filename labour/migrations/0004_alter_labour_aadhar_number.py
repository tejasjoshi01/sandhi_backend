# Generated by Django 3.2.5 on 2021-07-06 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labour', '0003_auto_20210706_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labour',
            name='aadhar_number',
            field=models.IntegerField(),
        ),
    ]

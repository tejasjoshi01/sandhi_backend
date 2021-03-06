# Generated by Django 3.2.5 on 2021-07-09 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labour', '0005_alter_labour_aadhar_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer_full_name', models.CharField(max_length=250)),
                ('skill_required', models.CharField(choices=[('ELECTRICIAN', 'ELECTRICIAN'), ('PLUMBER', 'PLUMBER'), ('LABOUR', 'LABOUR'), ('DRIVER', 'DRIVER'), ('MAID', 'MAID'), ('SECURITY GUARD', 'SECURITY GUARD'), ('COOK', 'COOK'), ('MECHANIC', 'MECHANIC'), ('PEON', 'PEON'), ('OTHERS', 'OTHERS')], default='OTHERS', max_length=20)),
                ('location', models.CharField(max_length=255)),
                ('pincode', models.IntegerField()),
                ('employer_contact', models.IntegerField(unique=True)),
                ('message', models.TextField()),
            ],
        ),
    ]

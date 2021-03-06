# Generated by Django 3.2.5 on 2021-07-20 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labour', '0008_alter_job_employer_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labour',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='labour',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='labour',
            name='aadhar_number',
            field=models.BigIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='labour',
            name='contact_number',
            field=models.BigIntegerField(unique=True),
        ),
    ]

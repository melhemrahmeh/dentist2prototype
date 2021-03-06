# Generated by Django 4.0.1 on 2022-01-30 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctordashboard', '0002_remove_patient_gender_alter_patient_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='cause',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='operation_price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

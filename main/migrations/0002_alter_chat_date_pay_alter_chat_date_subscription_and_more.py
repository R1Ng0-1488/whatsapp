# Generated by Django 4.0.2 on 2022-02-16 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='date_pay',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='date_subscription',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='date_trial',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='phone',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='platform',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

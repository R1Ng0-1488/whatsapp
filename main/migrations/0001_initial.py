# Generated by Django 4.0.2 on 2022-02-15 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('instanceId', models.CharField(max_length=100)),
                ('token', models.CharField(max_length=100)),
                ('chat_id', models.CharField(max_length=100)),
                ('md', models.IntegerField()),
                ('chat_token', models.CharField(max_length=100)),
                ('chat_key', models.CharField(max_length=100)),
                ('apikey', models.CharField(max_length=100)),
                ('date_add', models.CharField(max_length=100)),
                ('date_trial', models.CharField(max_length=100)),
                ('date_pay', models.CharField(max_length=100)),
                ('date_subscription', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('platform', models.CharField(max_length=100)),
                ('status', models.IntegerField()),
                ('is_premium', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Чат',
                'verbose_name_plural': 'Чаты',
            },
        ),
    ]

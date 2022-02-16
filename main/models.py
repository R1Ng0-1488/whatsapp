from tabnanny import verbose
from django.db import models


class Chat(models.Model):
    id = models.IntegerField(primary_key=True)
    instanceId = models.CharField(max_length=100)
    token = models.CharField(max_length=100)
    chat_id = models.CharField(max_length=100)
    md = models.IntegerField()
    chat_token = models.CharField(max_length=100)
    chat_key = models.CharField(max_length=100)
    apikey = models.CharField(max_length=100)
    date_add = models.CharField(max_length=100)
    date_trial = models.CharField(max_length=100, null=True)
    date_pay = models.CharField(max_length=100, null=True)
    date_subscription = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    platform = models.CharField(max_length=100, null=True)
    status = models.IntegerField()
    is_premium = models.BooleanField()

    def __str__(self):
        return f'{self.id}'
    

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
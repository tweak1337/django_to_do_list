from django.contrib.auth.models import User
from django.db import models


class ActiveList(models.Model):
    deal = models.CharField(max_length=58, verbose_name='Дело')
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_done = models.BooleanField(default=False, verbose_name='Выполнено')
    done_date = models.DateTimeField(null=True, verbose_name='Дата добавления')
    days = models.IntegerField(null=True, verbose_name='Дней выполнения')
    hours = models.IntegerField(null=True, verbose_name='Часов выполнения')
    minutes = models.IntegerField(null=True, verbose_name='Минут выполнения')
    seconds = models.IntegerField(null=True, verbose_name='Секунд выполнения')

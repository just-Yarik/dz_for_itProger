from django.db import models
from django.utils import timezone 

# Create your models here.
class Shopers (models.Model):
    name = models.CharField('Ім`я кліента:',max_length=100)
    surname = models.CharField('Призвісько кліента:',max_length=100)
    gmail = models.CharField('Електронна скринька кліента:',max_length=200)
    date = models.DateTimeField (default=timezone.now)

# def __str__(self):
#     return f'{self.surname}'

# class Meta:
#  verbose_name = 'Кліент'
#  verbose_name_plural = 'Кліенти'

# У мене чомусь не хочуть переіміновуватись назви для стовбця
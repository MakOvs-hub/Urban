from django.db import models

# Create your models here.

class Buyer(models.Model): # модель представляющая покупателя.
    name = models.CharField(max_length=30) # имя покупателя(username аккаунта)
    balance = models.DecimalField(max_digits=100000, decimal_places=1) # баланс(DecimalField - поле для дробных чисел)
    age = models.IntegerField(max_length=3) #возраст

    def __str__(self):
        return self.name


class Game(models.Model): # модель представляющая игру.
    title = models.CharField(max_length=50) # название игры
    cost = models.DecimalField(max_digits=100000, decimal_places=1) #цена(DecimalField - поле для дробных чисел)
    size = models.DecimalField(max_digits=100000, decimal_places=1) #размер файлов игры(DecimalField - поле для дробных чисел)
    description = models.TextField() #описание(неограниченное кол-во текста)
    age_limited = models.BooleanField(default=False) # ограничение возраста 18+ (BooleanField, по умолчанию False)
    buyer = models.ManyToManyField(Buyer, related_name='games') #покупатель обладающий игрой (ManyToManyField).
                                    # У каждого покупателя может быть игра и у каждой игры может быть несколько обладателей.
    def __str__(self):
        return self.title
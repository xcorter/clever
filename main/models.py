from django.db import models

class Game(models.Model):
    leading = models.CharField(max_length=400, verbose_name="Ведущий")
    date_time = models.DateTimeField(verbose_name="Время")
    money = models.IntegerField(verbose_name="Сумма")

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"

class Question(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name="Номер вопроса")
    question = models.TextField(verbose_name="Вопрос", default="")

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200, verbose_name="Ответ")
    is_correct = models.BooleanField(default=False, verbose_name="Правильный вопрос")

import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    q_title = models.CharField('Имя: ',max_length=255)
    q_text = models.TextField('Вопрос: ')
    q_date = models.DateTimeField('Дата публикации: ')

    def __str__(self):
        return self.q_title

    def was_published_recently(self):
        return self.q_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Comment(models.Model):
    article = models.ForeignKey(Question, on_delete=models.CASCADE)
    author_name = models.CharField('Имя автора: ', max_length=55)
    comment_text = models.TextField('Текст комментария: ', max_length=200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Коментарий к вопросу'
        verbose_name_plural = 'Коментарии к вопросам'


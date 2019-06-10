from django.db import models


class Blog(models.Model):

    text = models.TextField(verbose_name='Текст блога')

    def __str__(self):
        return 'Блог №{}'.format(self.id)

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'
        db_table = 'anonymous_blog'

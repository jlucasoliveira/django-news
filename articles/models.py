from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    title = models.CharField('Título', max_length=255)
    body = models.TextField('Corpo')
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), verbose_name='Autor', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:detail', args=(str(self.id),))

    class Meta:
        verbose_name = 'Artigo'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                verbose_name='Artigo', related_name='comments')
    comment = models.CharField('Comentário', max_length=140)
    author = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article:detail', args=(str(self.article.pk),))

    class Meta:
        verbose_name = 'Comentário'

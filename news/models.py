from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Цена', max_length=6 )
    full_text = models.TextField ('Описание товара')
    date = models.DateTimeField('Дата публикации')
    image = models.ImageField(upload_to='images/', null=True, max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

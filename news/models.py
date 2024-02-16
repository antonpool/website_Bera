from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self', 
        related_name='children',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Цена', max_length=6 )
    full_text = models.TextField ('Описание товара')
    date = models.DateTimeField('Дата публикации')
    image = models.ImageField( "картинка", upload_to='images/', null=True, max_length=255)
    slug = models.SlugField('ссылка', max_length=100)
    category = models.ForeignKey(
        Category,
        related_name='post',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_absolute_url(self):
        return reverse("post_single", kwargs={"slug": self.category.slug, "post_slug":self.slug})    


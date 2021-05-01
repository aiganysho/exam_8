from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

categories = (['книги', 'books'], ['фрукты', 'fruit'], ['аксессуары', 'accessories'], ['разное', 'others'])


class Product(models.Model):
    name_product = models.CharField(blank=False, null=False, max_length=100, verbose_name='Наазвание')
    category = models.TextField(null=False, blank=False, choices=categories, verbose_name='Категория')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    picture = models.ImageField(upload_to='pictures', null=True, blank=True )

    class Meta:
        db_table = 'products'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.id}, {self.name_product}'


class Review(models.Model):
    author = models.ManyToManyField(get_user_model(), related_name='reviews', null=False, blank=False, verbose_name='Автор')
    product = models.ForeignKey(
        'webapp.Product',
        on_delete=models.CASCADE,
        related_name='product_review',
        null=False,
        blank=False
    )
    text_review = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Текст отзыва')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='Оценка')
    moderation = models.BooleanField(null=False, blank=False, verbose_name='Отмодерирован')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        db_table = 'reviews'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.author}: {self.text_review}'

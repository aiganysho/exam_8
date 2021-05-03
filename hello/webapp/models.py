from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg



# Create your models here.

categories = (['одежда', 'clothes'], ['фрукты', 'fruit'], ['аксессуары', 'accessories'], ['разное', 'others'])


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
        return f'{self.id} {self.name_product}'


    def get_avg_rating(self):
        avg_rating = Review.objects.all().aggregate(Avg('rating'))
        for rate in self.reviews.all():
             return round(avg_rating['rating__avg'], 1)


    # def get_avg_rating(self):
    #         review = Review.objects.all()
    #         count = len(review)
    #         sum = 0
    #         for review_avr in self.reviews.all():
    #             sum += review_avr.rating
    #         return (sum/count)


class Review(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name='reviews'
    )

    product = models.ForeignKey(
        'webapp.Product',
        on_delete=models.CASCADE,
        related_name='reviews',
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

    # def ratings(self):
    #     if self.rating is None:
    #         return 0
    #     else:
    #         return self.get_avg_rating
# coding: utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser



class BaseProjectModel(models.Model):
    """
    Базовая абстрактная модель c общими филдами для моделей проекта
    """
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        abstract = True


class CustomUser(AbstractUser, BaseProjectModel):
    """
    Кастомная модель юзера
    """
    pass


class Review(BaseProjectModel):
    """
    Модель отзывов в гостевой книге
    """
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField("Review text")

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ["-created_at"]

    def __str__(self):
        return str(self.id)


class Reply(BaseProjectModel):
    """
    Модель ответов на отзывы в гостевой книге
    """
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    text = models.TextField("Reply text")

    class Meta:
        verbose_name = "Reply"
        verbose_name_plural = "Replies"

    def __str__(self):
        return str(self.id)

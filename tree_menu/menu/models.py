from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='Название меню',
        unique=True
    )
    slug = models.SlugField(max_length=100, verbose_name='Slug', null=True)
    named_url = models.CharField(max_length=255, verbose_name='Именованный URL', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ['name']


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu, related_name='items',
        on_delete=models.CASCADE, verbose_name='Меню'
    )
    parent = models.ForeignKey(
        'self', related_name='children',
        on_delete=models.CASCADE, blank=True, null=True
    )
    name = models.CharField(max_length=50, verbose_name='Название пункта меню')
    named_url = models.CharField(
        max_length=255, verbose_name='Именованный URL',
        blank=True
    )
    url = models.CharField(max_length=255, verbose_name='Ссылка', blank=True)
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')
    level = models.IntegerField(default=0, verbose_name='Уровень')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        ordering = ['menu', 'level', 'name']

    def clean(self):
        if self.url and self.named_url:
            raise ValidationError(
                "Please specify EITHER a URL OR a named URL, not both."
            )

    def get_url(self):
        if self.named_url:
            return reverse(self.named_url)
        return self.url or '/'

    def save(self, *args, **kwargs):
        self.level = self.parent.level + 1 if self.parent else 0
        super().save(*args, **kwargs)

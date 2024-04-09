from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField(
        "Наименование меню",
        max_length=100
    )

    description = models.CharField(
        "Описание меню",
        max_length=300,
        blank=True,
        null=True
    )

    base_url = models.CharField(
        "Ссылка на меню",
        max_length=100,
        blank=True,
        null=False
    )

    def __str__(self):
        return self.name


class MenuItems(models.Model):

    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        "Наименование пункта меню",
        max_length=100
    )

    description = models.CharField(
        "Описание пункта меню",
        max_length=300,
        blank=True,
        null=True
    )

    link_url = models.CharField(
        "URL",
        max_length=100,
        help_text='URL'
    )

    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name='menu_items',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

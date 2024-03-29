# Generated by Django 4.2.9 on 2024-03-29 13:09

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DiscountCart",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100, verbose_name="название акции")),
                ("description", models.TextField(verbose_name="описание акции")),
                ("start_date", models.DateField(verbose_name="начало акции")),
                ("end_date", models.DateField(verbose_name="окончание акции")),
                ("is_active", models.BooleanField(default=True, verbose_name="статус активности скидки")),
                (
                    "weight",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=3,
                        validators=[
                            django.core.validators.MinValueValidator(0.01),
                            django.core.validators.MaxValueValidator(1.0),
                        ],
                        verbose_name="вес скидки",
                    ),
                ),
                ("percentage", models.PositiveIntegerField(default=0, verbose_name="процент скидки")),
                ("price_from", models.DecimalField(decimal_places=2, max_digits=10, verbose_name="диапазон цены от")),
                (
                    "price_to",
                    models.DecimalField(
                        decimal_places=2, default=Decimal("Infinity"), max_digits=10, verbose_name="диапазон цены до"
                    ),
                ),
            ],
            options={
                "verbose_name": "скидка на стоимость корзины",
                "verbose_name_plural": "скидки на стоимость корзины",
            },
        ),
        migrations.CreateModel(
            name="DiscountSet",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100, verbose_name="название акции")),
                ("description", models.TextField(verbose_name="описание акции")),
                ("start_date", models.DateField(verbose_name="начало акции")),
                ("end_date", models.DateField(verbose_name="окончание акции")),
                ("is_active", models.BooleanField(default=True, verbose_name="статус активности скидки")),
                (
                    "weight",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=3,
                        validators=[
                            django.core.validators.MinValueValidator(0.01),
                            django.core.validators.MaxValueValidator(1.0),
                        ],
                        verbose_name="вес скидки",
                    ),
                ),
                (
                    "discount_amount",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=6,
                        validators=[django.core.validators.MinValueValidator(1.0)],
                        verbose_name="размер скидки",
                    ),
                ),
                ("first_group", models.ManyToManyField(related_name="first_group", to="products.product")),
                ("second_group", models.ManyToManyField(related_name="second_group", to="products.product")),
            ],
            options={
                "verbose_name": "скидка на набор товаров",
                "verbose_name_plural": "скидки на наборы товаров",
            },
        ),
        migrations.CreateModel(
            name="DiscountProduct",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100, verbose_name="название акции")),
                ("description", models.TextField(verbose_name="описание акции")),
                ("start_date", models.DateField(verbose_name="начало акции")),
                ("end_date", models.DateField(verbose_name="окончание акции")),
                ("is_active", models.BooleanField(default=True, verbose_name="статус активности скидки")),
                (
                    "weight",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=3,
                        validators=[
                            django.core.validators.MinValueValidator(0.01),
                            django.core.validators.MaxValueValidator(1.0),
                        ],
                        verbose_name="вес скидки",
                    ),
                ),
                ("percentage", models.PositiveIntegerField(default=0, verbose_name="процент скидки")),
                ("products", models.ManyToManyField(related_name="discount_products", to="products.product")),
            ],
            options={
                "verbose_name": "скидка на товар",
                "verbose_name_plural": "скидки на товары",
            },
        ),
    ]

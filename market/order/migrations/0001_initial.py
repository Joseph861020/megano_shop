# Generated by Django 4.2.11 on 2024-04-15 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("cart", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.TextField(max_length=20, verbose_name="имя")),
                ("phone", models.IntegerField(verbose_name="телефон")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="дата создания")),
                (
                    "delivery_type",
                    models.CharField(
                        choices=[("regular", "Обычная доставка"), ("express", "Экспресс-доставка")],
                        default="regular",
                        max_length=50,
                        verbose_name="delivery type",
                    ),
                ),
                ("city", models.CharField(max_length=50, verbose_name="город")),
                ("address", models.CharField(max_length=255, verbose_name="адрес")),
                (
                    "payment_type",
                    models.CharField(
                        choices=[("card", "Онлайн картой")],
                        default="card",
                        max_length=50,
                        verbose_name="Способ оплаты",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("created", "Создан"), ("paid", "Оплачен"), ("not_paid", "Не оплачен")],
                        default="created",
                        max_length=15,
                        verbose_name="статус",
                    ),
                ),
                ("total_price", models.DecimalField(decimal_places=2, max_digits=12, verbose_name="Общая стоимость")),
                (
                    "cart",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="cart.cart", verbose_name="корзина"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "заказ",
                "verbose_name_plural": "заказы",
                "db_table": "order",
            },
        ),
    ]

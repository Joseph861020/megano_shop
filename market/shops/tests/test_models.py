from django.test import TestCase

from products.models import Product, Category
from shops.models import Shop, Offer
from accounts.models import User


class ShopModelTest(TestCase):
    """Класс тестов модели Магазин"""

    fixtures = ["04-shops.json", "02-users.json"]

    def test_fixture_loading(self):
        shop_count = Shop.objects.count()
        print(f"Actual shop count: {shop_count}")
        self.assertEqual(shop_count, 9)

    def test_shop_user_relation(self):
        shops = Shop.objects.all()
        for shop in shops:
            user_id = shop.user_id
            user = User.objects.get(pk=user_id)
            self.assertIsNotNone(user, f"User with id {user_id} not found for shop {shop.name}")

    @classmethod
    def setUpTestData(cls):
        cls.product = Product.objects.create(
            name="тестовый продукт",
            category_id=1,
            details={"Диагональ, дм": 101},
        )
        cls.shop = Shop.objects.create(name="тестовый магазин")
        cls.offer = Offer.objects.create(shop=cls.shop, product=cls.product, price=25)

    def test_verbose_name(self):
        shop = ShopModelTest.shop
        field_verboses = {
            "name": "название",
            "products": "товары в магазине",
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(shop._meta.get_field(field).verbose_name, expected_value)

    def test_name_max_length(self):
        shop = ShopModelTest.shop
        max_length = shop._meta.get_field("name").max_length
        self.assertEqual(max_length, 512)


class OfferModelTest(TestCase):
    """Класс тестов модели Предложение магазина"""

    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name="TestCategory")
        cls.product = Product.objects.create(
            name="тестовый продукт",
            category=cls.category,
            details={"Диагональ, дм": 101},
        )
        cls.shop = Shop.objects.create(name="тестовый магазин")
        cls.offer = Offer.objects.create(shop=cls.shop, product=cls.product, price=35)

    def test_verbose_name(self):
        offer = OfferModelTest.offer
        field_verboses = {
            "price": "цена",
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(offer._meta.get_field(field).verbose_name, expected_value)

    def test_price_max_digits(self):
        offer = OfferModelTest.offer
        max_digits = offer._meta.get_field("price").max_digits
        self.assertEqual(max_digits, 10)

    def test_price_decimal_places(self):
        offer = OfferModelTest.offer
        decimal_places = offer._meta.get_field("price").decimal_places
        self.assertEqual(decimal_places, 2)

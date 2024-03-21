""" Модуль с представлениями приложения cart """
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from cart.cart import CartInstance
from cart.forms import CartUpdateProductForm
from shops.models import Offer


class CartView(TemplateView):
    """Представление для отображения корзины"""

    template_name = "cart/cart.jinja2"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = CartInstance(self.request)
        for item in cart:
            item["form"] = CartUpdateProductForm(initial={"quantity": item["quantity"], "update": False})
        context["cart"] = cart
        return context


@require_POST
def cart_add(request: HttpRequest, pk: int) -> HttpResponse:
    """Добавление товара в корзину"""

    cart = CartInstance(request)
    offer = get_object_or_404(Offer, id=pk)
    form = CartUpdateProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(offer, quantity=cd["quantity"], update_quantity=cd["update"])

    return redirect(request.META.get("HTTP_REFERER"))


@require_POST
def cart_remove(request, pk):
    """Удаление товара из корзины"""
    cart = CartInstance(request)
    offer = get_object_or_404(Offer, id=pk)
    cart.remove(offer)
    return redirect("cart:cart")

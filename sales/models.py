from django.db import models
from django.conf import settings
from django.utils import timezone

from inventory.models import Product


class Sale(models.Model):
    sale_date = models.DateTimeField(
        default=timezone.now, verbose_name="Fecha de Venta"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sales",
        verbose_name="Vendedor",
    )
    total_usd = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Total USD"
    )
    total_bs = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Total BS"
    )
    notes = models.TextField(blank=True, null=True, verbose_name="Notas")

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        ordering = ["-sale_date"]

    def __str__(self):
        return f"Venta #{self.pk} - {self.sale_date.strftime('%d/%m/%Y %H:%M')}"


class SaleItem(models.Model):
    sale = models.ForeignKey(
        Sale, on_delete=models.CASCADE, related_name="items", verbose_name="Venta"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Producto",
    )
    quantity = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Cantidad"
    )
    unit_price_usd = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Precio Unitario USD"
    )
    unit_price_bs = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Precio Unitario BS"
    )
    subtotal_usd = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Subtotal USD"
    )

    class Meta:
        verbose_name = "Ítem de Venta"
        verbose_name_plural = "Ítems de Venta"

    def __str__(self):
        return f"{self.quantity} x {self.product.name} en Venta #{self.sale.pk}"

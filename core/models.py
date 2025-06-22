from django.db import models
from django.utils import timezone


class CurrencyExchangeRate(models.Model):
    class Currency(models.TextChoices):
        USD = "USD", "Dólar Estadounidense"
        EUR = "EUR", "Euro"
        BS = "BS", "Bolívar Venezolano"

    date = models.DateField(
        default=timezone.now,
        verbose_name="Fecha de la Tasa",
        help_text="La fecha a la que aplica esta tasa de cambio.",
    )
    from_currency = models.CharField(
        max_length=10,
        choices=Currency.choices,
        default=Currency.USD,
        verbose_name="Moneda Origen",
        help_text="La moneda de la cual se está convirtiendo (ej. USD).",
    )
    to_currency = models.CharField(
        max_length=10,
        choices=Currency.choices,
        default=Currency.BS,
        verbose_name="Moneda Destino",
        help_text="La moneda a la cual se está convirtiendo (ej. BS).",
    )
    rate = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Tasa de Cambio",
        help_text="Valor: 1 USD = X BS.",
    )
    currency = models.CharField(
        max_length=10,
        choices=Currency.choices,
        default=Currency.USD,
        help_text="Moneda",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Registro"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Última Actualización del Registro"
    )

    def __str__(self):
        return f"1 {self.get_from_currency_display()} = {self.rate} {self.get_to_currency_display()} ({self.date.strftime('%d/%m/%Y')})"

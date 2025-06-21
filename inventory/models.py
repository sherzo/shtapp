from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100, unique=True, verbose_name="Nombre de la Categoría"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")

    class Unit(models.TextChoices):
        UNIT = "unit", "Unidad"
        CENTIMETER = "cm", "Centímetro"
        METER = "m", "Metro"
        KILOGRAM = "kg", "Kilogramo"
        LITER = "l", "Litro"

    unit_of_measure = models.CharField(
        max_length=10,
        choices=Unit.choices,
        default=Unit.UNIT,
        help_text="Unidad de Medida",
    )
    stock = models.IntegerField(default=0, verbose_name="Stock")
    sku = models.CharField(
        max_length=20,
        unique=True,
        db_index=True,
        verbose_name="SKU",
        help_text="Stock Keeping Unit - Código único para el producto y su variante.",
    )
    selling_price_usd = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Precio de Venta (USD)"
    )
    purchase_price_usd = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        verbose_name="Precio de Compra (USD)",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
        verbose_name="Categoría",
    )
    low_stock_threshold = models.IntegerField(
        default=0,
        verbose_name="Umbral de Stock Bajo",
        help_text="Nivel de stock en el que el producto se considera 'bajo'.",
    )
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["name"]

    def __str__(self):
        return self.name

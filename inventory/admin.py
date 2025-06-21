from django.contrib import admin

from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = (
        "created_at",
        "updated_at",
    )
    ordering = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "sku",
        "stock",
        "unit_of_measure",
        "selling_price_usd",
        "category",
        "is_active",
        "created_at",
        "updated_at",
    )

    search_fields = ("name", "sku", "description")

    list_filter = (
        "is_active",
        "category",
        "unit_of_measure",
        "created_at",
        "updated_at",
    )

    list_editable = ("stock", "selling_price_usd", "is_active")

    list_display_links = ("name", "sku")

    raw_id_fields = ("category",)

    fieldsets = (
        (
            None,
            {"fields": (("name", "sku"), "description", ("stock", "unit_of_measure"))},
        ),
        (
            "Información de Precios",
            {"fields": (("purchase_price_usd", "selling_price_usd"),)},
        ),
        (
            "Organización y Estado",
            {
                "fields": (
                    "category",
                    "is_active",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Fechas",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
                "classes": ("collapse",),
                "description": "Fechas de creación y última actualización del registro.",
            },
        ),
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = ("name",)

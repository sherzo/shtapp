from django.contrib import admin

from .models import Sale, SaleItem


class SaleItemInline(admin.TabularInline):
    model = SaleItem
    extra = 0
    fields = (
        "product",
        "quantity",
        "unit_price_usd",
        "unit_price_bs",
        "subtotal_usd",
    )


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "sale_date",
        "user",
        "total_usd",
        "total_bs",
        "notes",
    )

    list_filter = (
        "sale_date",
        "user",
    )

    search_fields = (
        "id",
        "user__username",
        "notes",
    )

    readonly_fields = (
        "total_usd",
        "total_bs",
        "sale_date",
    )

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user",
                    "notes",
                )
            },
        ),
        (
            "Detalles Financieros",
            {
                "fields": (
                    "total_usd",
                    "total_bs",
                ),
                "description": "Estos totales se calculan automáticamente y no son editables directamente.",
            },
        ),
        (
            "Fechas",
            {
                "fields": ("sale_date",),
                "classes": ("collapse",),
            },
        ),
    )

    inlines = [SaleItemInline]

    ordering = ("-sale_date",)

    def save_model(self, request, obj, form, change):
        if (
            not obj.user_id
        ):  # Si el vendedor no ha sido establecido (es una nueva venta)
            obj.user = request.user  # Asigna el usuario logueado como vendedor
        super().save_model(request, obj, form, change)

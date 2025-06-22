from django.contrib import admin

from .models import CurrencyExchangeRate


@admin.register(CurrencyExchangeRate)
class CurrencyExchangeRateAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "from_currency",
        "to_currency",
        "rate",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "from_currency",
        "to_currency",
        "date",
    )
    search_fields = (
        "from_currency",
        "to_currency",
        "rate",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "-date",
        "from_currency",
        "to_currency",
    )

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "from_currency",
                    "to_currency",
                    "rate",
                    "date",
                )
            },
        ),
        (
            "Información de Registro",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
                "classes": ("collapse",),
            },
        ),
    )

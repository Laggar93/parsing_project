from django.contrib import admin
from .models import GoodsModel


class GoodsModelAdmin(admin.ModelAdmin):
    list_display = ('code',)


admin.site.register(GoodsModel, GoodsModelAdmin)

from django.contrib import admin

from .models import CardType, Card


class CardTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'card_type', 'mana_cost', 'life', 'damage', 'modified')
    list_filter = ('card_type', 'mana_cost')

admin.site.register(CardType, CardTypeAdmin)
admin.site.register(Card, CardAdmin)

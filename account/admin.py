from django.contrib import admin

from .models import Account, Transaction, Journal, Tag

class AccountAdmin(admin.ModelAdmin):
    list_display = ('category', 'name')

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('text', )

admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Journal)
admin.site.register(Tag)

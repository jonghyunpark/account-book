from django.contrib import admin

from .models import Account, Transaction, Journal, Tag

class AccountAdmin(admin.ModelAdmin):
    list_display = ('category', 'name')

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('text', )

class JournalAdmin(admin.ModelAdmin):
    list_display = ('user_key', 'group', 'debit', 'credit', 'name', 'amount', 'transaction_date')

admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Journal, JournalAdmin)
admin.site.register(Tag)

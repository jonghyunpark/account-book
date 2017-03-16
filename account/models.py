from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

class Account(models.Model):
    ASSETS = "As"
    LIABILITIES = "Li"
    EQUITY = "Eq"
    EXPENSE = "Ex"
    INCOME = "In"
    CATEGORY_CHOICES = ((ASSETS, u'자산'),(LIABILITIES, u'부채'),
        (EQUITY, u'자본'),(EXPENSE, u'비용'),(INCOME, u'수익'))

    user_key = models.ForeignKey(User)
    category = models.CharField(max_length=2,
        choices=CATEGORY_CHOICES,
        default=ASSETS,)
    name = models.CharField(max_length=64)
    create_date = models.DateTimeField('created', auto_now_add=True)
    update_date = models.DateTimeField('updated', auto_now=True)

    def __str__(self):
        return "%d. %s" % (self.id, self.name[:80])

class Transaction(models.Model):
    user_key = models.ForeignKey(User)
    text = models.TextField(blank=True)
    transaction_date = models.DateTimeField('transaction date', auto_now=True)
    create_date = models.DateTimeField('created date', auto_now_add=True)
    update_date = models.DateTimeField('updated date', auto_now=True)

    def __str__(self):
        return "%d. %s" % (self.id, self.text[:80])

class Journal(models.Model):
    user_key = models.ForeignKey(User)
    group = models.ForeignKey('self', blank=True, null=True)
    debit = models.ForeignKey(Account, null=True, related_name='debit')
    credit = models.ForeignKey(Account, null=True, related_name='credit')
    name = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    create_date = models.DateTimeField('date created', auto_now_add=True)
    update_date = models.DateTimeField('date updated', auto_now=True)

    tags = models.ManyToManyField(Account,related_name='tag')


    def __str__(self):
        return "%d. %s" % (self.id, self.name[:80])

class Tag(models.Model):
    user_key = models.ForeignKey(User)
    text = models.TextField(blank=True)
    slug = models.SlugField(max_length=40)
    create_date = models.DateTimeField('date created', auto_now_add=True)
    update_date = models.DateTimeField('date updated', auto_now=True)

    def __str__(self):
        return "%d. %s" % (self.id, self.text[:80])

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.text)

        super(Tag, self).save(*args, **kwargs)
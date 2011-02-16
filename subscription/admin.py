from django.contrib import admin
from subscription.models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')

admin.site.register(Subscription, SubscriptionAdmin)


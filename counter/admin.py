from django.contrib import admin
from .models import Quote


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('text', 'days_count', 'submission_time', 'approved')
    list_filter = ('approved', 'submission_time')
    search_fields = ('text',)

from django.contrib import admin
from django.db import models
from django.forms import Textarea
from .models import Quote


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('text', 'days_count', 'submission_time', 'approved')
    list_filter = ('approved', 'submission_time')
    search_fields = ('text',)
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 8, 'cols': 80})},
    }

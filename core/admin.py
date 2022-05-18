from django.contrib import admin
from core.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'event_date', 'created_at')
    # list_filter = ('event_date',)
    # search_fields = ('title', 'description')

# Register your models here.
admin.site.register(Event, EventAdmin)
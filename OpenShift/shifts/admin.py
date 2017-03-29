from django.contrib import admin

# below is created by me
from django.contrib import admin
from .models import open_shift

class ShiftAdmin(admin.ModelAdmin):
    list_display = ('date', 'start','end','description','is_filled', 'is_sent')
    search_fields = ('date', 'is_filled','is_sent')
    list_filter = ('date', 'is_filled','is_sent',)
    ordering = ('-date',)


admin.site.register(open_shift, ShiftAdmin)

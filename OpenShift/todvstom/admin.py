from django.contrib import admin

# Register your models here.
from .models import Room

class RoomsAdmin(admin.ModelAdmin):
	list_display = ['set_date','symph_a', 'symph_b',
					'ballroom','mozart','beethoven',
					'board','handel','haydn','capitol',
					'other']
	search_fields = ['date']
	list_filter = ['set_date']
	ordering = ['-set_date']

admin.site.register(Room, RoomsAdmin)
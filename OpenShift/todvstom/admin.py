from django.contrib import admin

# Register your models here.
from .models import Rooms

class RoomsAdmin(admin.ModelAdmin):
	list_display = ['set_date','symph_a', 'symph_b',
					'ballroom','mozart','beethoven',
					'board','handel','haydn','capitol',
					'other']

admin.site.register(Rooms, RoomsAdmin)
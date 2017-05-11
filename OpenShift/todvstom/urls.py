from django.conf.urls import urls
from . import views

urlpatterns = [
	url(r'room_sets/', views.room_sets, name = 'room_sets')
]
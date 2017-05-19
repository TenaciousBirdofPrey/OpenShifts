from django.conf.urls import urls
from . import views

urlpatterns = [
	url(r'room_sets/', views.room_sets, name = 'room_sets'),
	url(r'^seven_day', views.room_sets, name = 'seven_day'),
	url(r'^seven_day_pick/', todvstom.views.seven_day_pick, name = 'seven_day_pick'),
]
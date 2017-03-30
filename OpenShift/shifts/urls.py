#blank file created by me
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	#parking_train
	url(r'parking_train/', views.parking_train, name = 'parking_train'),
]
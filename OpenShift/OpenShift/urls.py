"""OpenShift URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# added by me:
# Log in/out

# point root URLconf at the shifts.urls module.
from django.conf.urls import include
# needed to establish view and template?
import shifts.views
# import views from today vs tommorow
import todvstom.views


urlpatterns = [
	#added by me:
    #Today vs Tommorow app
    url(r'^room_sets', todvstom.views.room_sets, name = 'room_sets'),
    url(r'^seven_day', todvstom.views.seven_day, name = 'seven_day'),



	#point root URLconf at shifts.urls module using imported include
	url(r'^shifts/', include('shifts.urls')),

    #makes index a view from shifts- such that localhost:8000 is at first page.
    url(r'^$', shifts.views.index, name = 'index'),

    #Blast Shifts-DET only
    url(r'^blast_shifts/', shifts.views.blast_shifts, name = 'blast_shifts'),
    url(r'^blast_confirm/', shifts.views.blast_confirm, name = 'blast_confirm'),

    #link to parking_train.html
    url(r'^parking_train/', shifts.views.parking_train, name = 'parking_train'),
    url(r'^hotel_location/', shifts.views.hotel_location, name = 'hotel_location'),
    url(r'^parking/', shifts.views.parking, name = 'parking'),
    url(r'^train/', shifts.views.train, name = 'train'),


    #each_shift as url
    url(r'^shift/([0-9]+)', shifts.views.each_shift, name = 'each_shift'),

    #post confirm shift per per Ascent TV Tut
    url(r'^shift/post_url/([0-9]+)', shifts.views.post_confirm, name = 'post_confirm'),

    #allauth
    url(r'^accounts/', include('allauth.urls')),

	#not added by me.
    url(r'^admin/', admin.site.urls),
]

# Change admin site title
admin.site.site_header = ("PSAV 3571 ADMINISTRATION")
admin.site.site_title = ("3571 Admin")

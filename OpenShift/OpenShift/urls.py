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
# point root URLconf at the shifts.urls module.
from django.conf.urls import include
# needed to establish view and template?
import shifts.views


urlpatterns = [
	#added by me:


	#point root URLconf at shifts.urls module using imported include
	url(r'^shifts/', include('shifts.urls')),

    #makes index a view from shifts- such that localhost:8000 is at first page.
    url(r'^$', shifts.views.index, name = 'index'),


	#not added by me.
    url(r'^admin/', admin.site.urls),
]

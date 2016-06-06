"""poe_trader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
zz                                                                    z             zzFunction views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from trades.views import TradeViewSet, CurrencyViewSet
from portal.views import landing

router = routers.DefaultRouter()
router.register(r'trades', TradeViewSet)
router.register(r'currencies', CurrencyViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'api/', include(router.urls)),
    url(r'^', landing, name='home'),
]

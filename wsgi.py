"""
WSGI config for poe_trader project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

# Fix django closing connection to Caching Service after every request (#11331)
# from django.core.cache.backends.memcached import BaseMemcachedCache
# BaseMemcachedCache.close = lambda self, **kwargs: None

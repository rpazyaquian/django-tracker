"""
WSGI config for apptrack project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apptrack.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()




# Heroku config -- comment me out to work locally, uncomment to deploy on Heroku (is there a better solution?)

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
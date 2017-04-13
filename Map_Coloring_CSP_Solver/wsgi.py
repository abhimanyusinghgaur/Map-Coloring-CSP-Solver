"""
WSGI config for Map_Coloring_CSP_Solver project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Map_Coloring_CSP_Solver.settings")

application = get_wsgi_application()

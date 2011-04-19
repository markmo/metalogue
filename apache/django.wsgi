import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'metalogue.settings'

import django.core.handler.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

path = '/home/bitnami/apps/metalogue'
if path not in sys.path:
  sys.path.append(path)
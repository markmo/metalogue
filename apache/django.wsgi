import os
import sys

path = '/home/bitnami/apps/metalogue'
if path not in sys.path:
  sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'metalogue.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

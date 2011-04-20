import os
import sys

apps_path = '/home/bitnami/apps'
if apps_path not in sys.path:
  sys.path.append(apps_path)
project_path = '/home/bitnami/apps/metalogue'
if project_path not in sys.path:
  sys.path.append(project_path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'metalogue.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
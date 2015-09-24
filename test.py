#!/usr/bin/env python
from django.core.management import call_command
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_site.settings")
call_command('test', 'promises_instances', 'ddah_web', 'backend', verbosity=1)

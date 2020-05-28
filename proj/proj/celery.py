from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default DJango settings module for the celery program
# The line below is not needed but it saves you from always 
# passing in the setting module to the celery program 
# It must always come before creating the app instanes 
# app = Celery('proj')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")

app = Celery('proj')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# ---
# The uppercase name-space means that all Celery configuration options
# must be specified in uppercase instead of lowercase, and start with 
# CELERY
# e.g. task_always_eager will be CELERY_TASK_ALWAYS_EAGER
#       broker_url setting becoems CELERY_BROKER_URL
# This also applies to the workers settings, worker_concurrency setting 
# becomes CELERY_WORKER_CONCURRENCY
# The namespace is recommeded to prevent overlap with other
# Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
# This always each app to have their tasks, celery will locate them all
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
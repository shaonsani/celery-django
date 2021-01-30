from __future__ import absolute_import, unicode_literals
from celery.schedules import crontab
import os
from celery import Celery

tempVar = 15

os.environ.setdefault('DJANGO_SETTINGS_MODULE','Celery.settings')
app = Celery('Celery')
app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule={
    'first_day':{
        'task':'testapp.tasks.test_task',
        'schedule':crontab(hour=0, minute=10,day_of_month='1'),
        'args':('shaon',)
    },
    'sixteenth_day':{
        'task':'testapp.tasks.test_task',
        'schedule':crontab(hour=0, minute=10,day_of_month='16'),
        'args':('shaon sani',)
    },
    'every_interval':{
        'task':'testapp.tasks.test_task',
        'schedule': tempVar,  #TestModel.objects.latest('id').time
        'args':('fromdb',)
    }
}
app.autodiscover_tasks()
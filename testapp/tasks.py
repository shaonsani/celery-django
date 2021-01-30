from __future__ import absolute_import, unicode_literals

from celery import shared_task

#dummy task
@shared_task
def add():
    return 100

@shared_task
def test_task(name):
    print('test task has been executed by scheduler')
    return f"hello {name} schedular"

from celery import task,platforms
platforms.C_FORCE_ROOT = True

@task()
def add(x, y):
    return x + y

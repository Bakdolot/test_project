from european_union.celery import app
from .models import Project

from datetime import date


@app.task()
def check_finished():
    objects = Project.objects.filter(is_finished=False)
    update_queries = []
    for obj in objects:
        if date.today() >= obj.completion_date:
            obj.is_finished = True
            update_queries.append(obj)
    if update_queries:
        Project.objects.bulk_update(update_queries, ['is_finished'])


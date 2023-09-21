from celery import Celery
from flask import current_app as app


# celery = Celery(app)
celery = Celery("Ticket", include=["tasks"])

class ContextTask(celery.Task):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)
        
broker_url = 'redis://localhost:6379/1'
result_backend = 'redis://localhost:6379/2'

celery.conf.update(
    broker_url=broker_url,
    result_backend=result_backend,
)
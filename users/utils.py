from datetime import datetime
from django.conf import settings

from apscheduler.schedulers.background import BackgroundScheduler

from . import models


def do_somenthing() -> None:
    print(models.CustomUser.objects.all())
    print(f"=== RODANDO EM {datetime.now()} EM {settings.TIME_ZONE}")
    return


def start_cron() -> None:
    schedule = BackgroundScheduler()
    schedule.add_job(do_somenthing, trigger='cron', second=45)
    schedule.start()
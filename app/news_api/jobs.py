"""
module contains scheduler for recurring jobs
"""

from apscheduler.schedulers.background import BackgroundScheduler
from .views import reset_upvotes


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        reset_upvotes, "cron", hour=0, id="reset_upvotes_001", replace_existing=True
    )
    scheduler.start()

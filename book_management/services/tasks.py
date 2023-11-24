from celery import shared_task
from .email import send_welcome_letter


@shared_task
def send_welcome_letter_task(user_id):
    return send_welcome_letter(user_id)

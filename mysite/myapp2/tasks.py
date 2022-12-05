from time import sleep
from celery import shared_task


@shared_task
def send_book(name, email):
    sleep(10)
    print("hola")
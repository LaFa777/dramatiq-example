import random
import time
import dramatiq

# Шаг 1. Подключаем dramatiq к брокеру
from dramatiq.brokers.rabbitmq import RabbitmqBroker

broker = RabbitmqBroker(url="amqp://127.0.0.1:29001")
dramatiq.set_broker(broker)


# шаг 2. Обозначаем кто тут consumer (aka worker) (aka actor)
@dramatiq.actor
def print_text(text):
    print(text)


@dramatiq.actor(max_retries=3, min_backoff=7000)
def print_text_with_random_error(text):
    if 5 == random.randint(0, 15):
        raise Exception
    print(text)


@dramatiq.actor(time_limit=4000)
def long_task_failure():
    time.sleep(5)


@dramatiq.actor(time_limit=4000)
def heavy_calculated():
    return random.randint(0, 100)


@dramatiq.actor(max_retries=3, min_backoff=7000)
def task_with_error():
    raise Exception


@dramatiq.actor(max_retries=3, min_backoff=7000)
def task_without_error():
    return "Hello world!"


@dramatiq.actor
def task_print_result(result):
    print(result)


@dramatiq.actor
def task_print_error(*err):
    print(err)
    print("Ну что ж...")

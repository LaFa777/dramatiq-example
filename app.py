from task import print_text, print_text_with_random_error, long_task_failure, task_print_error, \
    task_print_result, task_with_error, task_without_error

input("Тест асинхронного запуска задач")

for i in range(10):
    print_text.send(f"Async test {i}")

input("Тест синхронного запуска задач")

print_text("Sync test")

input("Тест когда некоторые из задач падают с ошибками")

for i in range(10):
    print_text_with_random_error.send(f"Error test {i}")

input("Тест долго работающей таски, которая падает по таймауту")

long_task_failure.send()

input("Колбеки для результатов")

task_with_error.send_with_options(
    on_failure=task_print_error,
)

task_without_error.send_with_options(
    on_success=task_print_result,
)

# input("Тест пула задачек которые возвращают результат")
#
# # # тут необходима некоторая настройка
# # result_backend = RedisBackend()  # ну или memcached
# # broker.add_middleware(Results(backend=result_backend))
# # dramatiq.set_broker(broker)
#
# g = group([
#     heavy_calculated.message(),
#     heavy_calculated.message(),
#     heavy_calculated.message(),
# ]).run()
# g.wait(timeout=1000)
# text = g.get_results(block=True, timeout=5_000)
# print(list(text))

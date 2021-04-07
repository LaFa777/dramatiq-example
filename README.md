# Пример работы с dramatiq на базе rabbitmq

1. Запускаем rabbitmq
    ```bash
    docker-compose up -d
    ```
   
1. Запускаем консьюмера
    ```bash
    dramatiq task
    ```
   
1. Выполняем сценарий симулирующий отправку данных
    ```bash
   python app.py
    ```

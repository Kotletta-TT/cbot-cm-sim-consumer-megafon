# cbot-cm-sim-consumer-megafon

Данный сервис-бот "слушает" очередь RabbitMQ на предмет сообщений содержащих информацию о транках, и записывает эти данные в БД

Для запуска необходимо изменить config.yaml введя свои данные 

Убедиться в работе RabbitMQ, MySQL

Запустить build `docker build -t simcards-consumer-build .`  
Запустить docker `docker run -it --rm --name simcards-consumer-bot simcards-consumer-build`


import time
import pika
import sys
import os
import json
from app.log_init import log_on
from models.models import Sim
from db.db_helper import Session
from config.conf import RABBIT_HOST, RABBIT_PORT, RABBIT_QUEUE, LOG_NAME

"""# Как то ускорить работу с БД (множественный коммит?)"""
"""# Защита от падения/отсутствия коннекта с БД"""

session = Session()
logger = log_on(LOG_NAME)


def init_read_db():
    db = {}
    temp_list = session.query(Sim).all()
    if len(temp_list) > 1:
        for row in temp_list:
            key = row.phone
            db[key] = row
    return db


def main():
    temp_db = init_read_db()
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBIT_HOST, port=RABBIT_PORT))
            logger.debug(f'Connect to RabbitMQ address: {RABBIT_HOST}')
            break
        except:
            logger.error(f'RabbitMQ CONNECTION ERROR: {RABBIT_HOST}')
            time.sleep(10)
            continue
    channel = connection.channel()
    channel.queue_declare(queue=RABBIT_QUEUE)

    def callback(ch, method, properties, body):
        message = json.loads(body)
        logger.info(f'Take simcard-message to send in DB object: {message["phone"]}')
        key = message["phone"]
        print(message)
        value = Sim(**message)
        if key in temp_db:
            temp_db[key].id_provider = value.id_provider if temp_db[key].id_provider != value.id_provider else temp_db[key].id_provider
            temp_db[key].active = value.active if temp_db[key].active != value.active else temp_db[key].active
            temp_db[key].balance = value.balance if temp_db[key].balance != value.balance else temp_db[key].balance
            temp_db[key].services = value.services if temp_db[key].services != value.services else temp_db[key].services
            temp_db[key].rate = value.rate if temp_db[key].rate != value.rate else temp_db[key].rate
            temp_db[key].minute_remain = value.minute_remain if temp_db[key].minute_remain != value.minute_remain else temp_db[key].minute_remain
            temp_db[key].minute_total = value.minute_total if temp_db[key].minute_total != value.minute_total else temp_db[key].minute_total
            temp_db[key].accured = value.accured if temp_db[key].accured != value.accured else temp_db[key].accured
            temp_db[key].subscr_fee = value.subscr_fee if temp_db[key].subscr_fee != value.subscr_fee else temp_db[key].subscr_fee
        else:
            temp_db[key] = value
        try:
            session.add(temp_db[key])
            session.commit()
        except Exception as e:
            print(e)
        logger.debug(f'Record simcard-message to DB object: {message["phone"]}')
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue=RABBIT_QUEUE, on_message_callback=callback)

    channel.start_consuming()


def app_run():
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

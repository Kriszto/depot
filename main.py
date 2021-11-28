import time
import logging
from confluent_kafka import Producer
import socket

conf = {'bootstrap.servers': "localhost:9092",
        'client.id': socket.gethostname()}
producer = Producer(conf)
topic = 'alma'

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info(f'process started')

for i in range(0,100):
    logging.info(f'processing... ({i})')
    time.sleep(1)
    producer.produce(topic, key="key", value="value")

logging.info(f'process ended')

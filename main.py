import logging
import os
import sys
from sys import argv

from confluent_kafka import Producer
from watchdog.events import FileSystemEvent

from csv_processor import process_csv
from entity import Entity
from csvwatcher import CsvWatcher

EVENT = 'event'


def setup_logging():
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.info(f'process started')


setup_logging()

kafka_host = sys.argv[2] if len(sys.argv) > 2 else 'localhost'
kafka_port = sys.argv[3] if len(sys.argv) > 3 else '9091'

logging.info(f'kafka host:port is {kafka_host}:{kafka_port}')

p = Producer({'bootstrap.servers': f'{kafka_host}:{kafka_port}',
              'queue.buffering.max.messages': 1000,
              'queue.buffering.max.ms': 500,
              'batch.num.messages': 50,
              })
logging.info(p)


def log_file_event(event: FileSystemEvent):
    logging.info(f'csv processing started: {event.src_path}')
    process_csv(event.src_path, send_entity)
    p.flush(30)
    logging.debug(f'archiving {event.src_path}')
    os.rename(event.src_path, event.src_path + ".processed")
    logging.info(f'csv processing finished: {event.src_path}')


def send_entity(e: Entity):
    p.produce('%s' % EVENT, key=e.transaction_id, value=e.to_json())
    p.poll(0)


def handler(signum, frame):
    p.flush(30)
    exit(1)


p.flush(30)

if __name__ == '__main__':
    w = CsvWatcher(argv[1], log_file_event)
    w.run()

p.flush(30)

exit(1)

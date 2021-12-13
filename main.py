import glob
import logging
import os
import sys
from sys import argv
from typing import Callable

from confluent_kafka import Producer
from watchdog.events import FileSystemEvent

from csv_processor import process_csv
from entity import Entity
from csv_watcher import CsvWatcher

EVENT = 'event'


def setup_logging():
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.info(f'process started')


setup_logging()

path = argv[1]
kafka_host = sys.argv[2] if len(sys.argv) > 2 else 'localhost'
kafka_port = sys.argv[3] if len(sys.argv) > 3 else '9091'

logging.info(f'kafka host:port is {kafka_host}:{kafka_port}')

p = Producer({'bootstrap.servers': f'{kafka_host}:{kafka_port}',
              'queue.buffering.max.messages': 1000,
              'queue.buffering.max.ms': 500,
              'batch.num.messages': 50,
              })


def exec_file_event(src_path: str):
    logging.info(f'csv processing started: {os.path.basename(src_path)}')
    process_csv(src_path, send_entity)
    p.flush(30)
    logging.info(f'archiving {os.path.basename(src_path)}')
    os.rename(src_path, src_path + ".processed")
    logging.info(f'csv processing finished: {src_path}')


def send_entity(e: Entity):
    p.produce('%s' % EVENT, key=e.transaction_id, value=e.to_json())
    p.poll(0)


def init_process(dir: str, callback: Callable):
    for fn in glob.glob(f'{dir}/*.csv'):
        callback(fn)


def handler(signum, frame):
    p.flush(30)
    exit(1)


if __name__ == '__main__':
    init_process(path, exec_file_event)
    w = CsvWatcher(path, exec_file_event)
    w.run()

p.flush(30)

exit(1)

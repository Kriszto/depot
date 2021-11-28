import time
import logging
from confluent_kafka import Producer
import socket

from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'localhost:9091'})
p.produce('light_bulb', key='hello', value='world werwr')
p.flush(30)
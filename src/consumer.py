# consumer.py
from kafka import KafkaConsumer
import json
consumer = KafkaConsumer(
    'posts',
    bootstrap_servers=['localhost:9093'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)
# print(consumer.config)
# note that this for loop will block forever to wait for the next message
for message in consumer:
    print(message)
    print(type(message.value))
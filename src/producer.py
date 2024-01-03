# producer.py
from kafka import KafkaProducer
from datetime import datetime
import json
producer = KafkaProducer(
    bootstrap_servers=['localhost:9093'],
    #auto_offset_reset='earliest',
    # group_id='my_group',
  #  enable_auto_commit=False,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
producer.send('posts', value={'author': 'Hammama', 'content': 'Kafka is cool!', 'created_at': datetime.now().isoformat()})
producer.flush()
print("message sent successfully")

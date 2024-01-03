
# Local Kafka Cluster

source: [Setting up Kafka on Docker for Local Development](https://hackernoon.com/setting-up-kafka-on-docker-for-local-development)


`pip install -r requirements.txt`

`python producer.py`
`python consumer.py`


### Kafka using KCat
`brew install kcat`

`docker-compose up -d`

`kcat -b localhost:9093 -L  # list all topics currently in kafka`

`kcat -b localhost:9093 -t test-topic -P  # producer`

`kcat -b localhost:9093 -t test-topic -C  # consumer`
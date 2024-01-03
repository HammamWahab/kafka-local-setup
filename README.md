# Local Kafka Cluster Setup
=========================

This guide will help you set up a local Kafka cluster for development using Docker and interact with it using Python scripts and KCat. This guide is based on the tutorial: [Setting up Kafka on Docker for Local Development](https://hackernoon.com/setting-up-kafka-on-docker-for-local-development).

## Prerequisites
-------------

Make sure you have the following installed on your machine:

*   Docker
*   Docker Compose
*   Python
*   KCat (Kafka Cat)
*   Homebrew (for KCat installation on macOS)

## Setting up Kafka on Docker
--------------------------

To set up a local Kafka cluster, follow these steps:

1.  Clone the repository and navigate to the project directory:
    
    
    `git clone https://github.com/HammamWahab/kafka-local-setup.git && cd kafka-local-setup`
    
2.  Start the Kafka cluster using Docker Compose:
    
    
    `docker-compose up -d`
    

Interacting with Kafka using Python
-----------------------------------

Run the following commands to interact with Kafka using Python scripts:

### Producer


`python src/producer.py`

This will start a Python Kafka producer that sends messages to the 'posts' in the local Kafka cluster.

### Consumer


`python src/consumer.py`

This will start a Python Kafka consumer that listens to the 'posts' in the local Kafka cluster.

## Interacting with Kafka using KCat
---------------------------------

If you prefer using KCat to interact with Kafka, follow these commands:

### Install KCat

On macOS, use Homebrew:


`brew install kcat`

### List all topics in Kafka



`kcat -b localhost:9093 -L`

### Producer



`kcat -b localhost:9093 -t test-topic -P`

This allows you to manually produce messages to the 'test-topic' in the local Kafka cluster.

### Consumer



`kcat -b localhost:9093 -t test-topic -C`

This allows you to manually consume messages from the 'test-topic' in the local Kafka cluster.

Feel free to explore and modify the Python scripts and KCat commands based on your specific use case.
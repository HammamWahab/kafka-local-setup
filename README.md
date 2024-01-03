`pip install -r requirements.txt`
`brew install kcat`
`docker-compose up -d`
`kcat -b localhost:9093 -L  # list all topics currently in kafka`
`kcat -b localhost:9093 -t test-topic -P  # producer`
`kcat -b localhost:9093 -t test-topic -C  # consumer`
from kafka.admin import KafkaAdminClient, NewTopic 

admin_client= KafkaAdminClient(
    bootstrap_servers="localhost:9093",
    client_id='test'


)
topic_list=[]
topic = NewTopic(name='posts_test', num_partitions=1, replication_factor=1)
topic_list.append(topic)
admin_client.create_topics(new_topics=topic_list, validate_only=False)
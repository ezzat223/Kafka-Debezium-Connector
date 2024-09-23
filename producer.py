from kafka import KafkaProducer
import json

if __name__ == '__main__':
    print("Starting Kafka Producer...")
    producer = KafkaProducer(
        bootstrap_servers = "localhost:9092",
        value_serializer = lambda v: json.dumps(v).encode('utf-8')
    )
    producer.send("Orders", "order3")
    producer.flush()
    print("Message produced.")
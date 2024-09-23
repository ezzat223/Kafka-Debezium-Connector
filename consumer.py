from kafka import KafkaConsumer
import json

if __name__ == '__main__':
    consumer = KafkaConsumer(
        'Orders',
        bootstrap_servers = "localhost:9092",
        value_deserializer = lambda m: json.loads(m.decode('ascii'))
    )
    for message in consumer:
        print("Message received:")
        print(str(message.value))
from kafka import KafkaConsumer

consumer = KafkaConsumer('student-grades', bootstrap_servers='localhost:9092', auto_offset_reset='earliest')

print("Consuming and printing items from Kafka topic \"student-grades\". Hit Ctrl+C to stop...\n")
for message in consumer:
    print(f"Received \"{message.value}\" from Kafka broker at localhost:9092")
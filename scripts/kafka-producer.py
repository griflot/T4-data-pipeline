from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('student-grades', b'{"name": "Stacy", "grade": "A"}')
producer.send('student-grades', b'{"name": "Franklin", "grade": "F"}')
producer.flush()
producer.close()
from kafka import KafkaConsumer
import sqlite3

connector = sqlite3.connect('studentGrades.db')
cursor = connector.cursor()

consumer = KafkaConsumer('student-grades', bootstrap_servers='localhost:9092', auto_offset_reset='earliest')

print("Consuming and printing items from Kafka topic \"student-grades\". Hit Ctrl+C to stop...")

def insert_into_db(student_name, grade):
    try:
        cursor.execute('''
            INSERT INTO studentGrades (student_name, grade)
            VALUES (?, ?)
        ''', (student_name, grade))
        connector.commit()
        print(f'Inserted {student_name} with grade {grade} into SQLite database.')
    except sqlite3.IntegrityError as e:
        print(f"Error inserting data: {e}")

for message in consumer:
    print(f"Received \"{message.value}\" from Kafka broker at localhost:9092")

    message_value = message.value.decode('utf-8')
    student_name, grade = message_value.split(',')

    insert_into_db(student_name.strip(), int(grade.strip()))
    
connector.close()

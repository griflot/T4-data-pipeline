from flask import Flask, request, jsonify
from kafka import KafkaProducer

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='localhost:9092')

@app.route('/send', methods=['POST'])
def send():
    data = request.get_json()
    name = data.get('name')
    grade = data.get('grade')
    json_msg = f'{{"name": "{name}", "grade": "{grade}"}}'

    producer.send('student-grades', json_msg.encode('utf-8'))
    producer.flush()

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(port=5000)

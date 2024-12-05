import pika
import json
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

# Setting up RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='filter_queue')

@app.route('/message', methods=['POST'])
def post_message():
    data = request.get_json()
    user = data.get('user', 'anonymous')
    initial_message = data.get('message', '')
    message = f"From user: {user}\nMessage: {initial_message}"
    message = json.dumps({'username': user, 'message': initial_message, 'timestamp': time.time()})
    
    # Publishing message to RabbitMQ
    channel.basic_publish(exchange='', routing_key='filter_queue', body=message)
    return jsonify({'status': 'success', 'message': 'Message received'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

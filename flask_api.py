import pika
from flask import Flask, request, jsonify

app = Flask(__name__)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='message_queue')

@app.route('/message', methods=['POST'])
def post_message():
    data = request.get_json()
    user = data.get('user', 'anonymous')
    initial_message = data.get('message', '')
    message = f"From user: {user}\nMessage: {initial_message}"
    
    channel.basic_publish(exchange='', routing_key='message_queue', body=message)
    return jsonify({'status': 'success', 'message': 'Message received'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

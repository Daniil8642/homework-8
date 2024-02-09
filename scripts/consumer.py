# consumer.py
import json
import time
from mongoengine import connect
from models.contact import Contact
import pika

# Підключення до MongoDB
connect('your_database_name', host='your_mongo_atlas_connection_string')

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='contact_queue')

def process_contact(contact_id):
    contact = Contact.objects(id=contact_id).first()
    if contact:
        # Імітація відправлення повідомлення по email
        print(f"Sending email to {contact.email}...")
        time.sleep(2)  # Імітація часу на відправку емейлу
        contact.message_sent = True
        contact.save()
        print(f"Email sent to {contact.email}.")

def callback(ch, method, properties, body):
    data = json.loads(body)
    contact_id = data.get('contact_id')
    if contact_id:
        process_contact(contact_id)

if __name__ == '__main__':
    channel.basic_consume(queue='contact_queue',
                          on_message_callback=callback,
                          auto_ack=True)
    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

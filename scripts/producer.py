# producer.py
import json
from faker import Faker
from mongoengine import connect
from models.contact import Contact
import pika

fake = Faker()

# Підключення до MongoDB
connect('your_database_name', host='your_mongo_atlas_connection_string')

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='contact_queue')

def generate_fake_contact():
    return {
        'full_name': fake.name(),
        'email': fake.email()
    }

def send_contact_to_queue(contact_id):
    channel.basic_publish(exchange='',
                          routing_key='contact_queue',
                          body=json.dumps({'contact_id': str(contact_id)}))
    print(f"Contact with ID {contact_id} sent to the queue.")

if __name__ == '__main__':
    for _ in range(5):  # Генерація 5 фейкових контактів
        fake_contact = generate_fake_contact()
        contact = Contact(**fake_contact).save()
        send_contact_to_queue(contact.id)

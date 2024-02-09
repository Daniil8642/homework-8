# main.py
from scripts import load_data, search_quotes
from producer import send_fake_contacts
from consumer import consume_messages

if __name__ == '__main__':
    # Завантаження даних до MongoDB
    load_data.load_authors()
    load_data.load_quotes()

    # Запуск скрипта producer.py
    send_fake_contacts()

    # Запуск скрипта consumer.py
    consume_messages()

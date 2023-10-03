"""
    producer code designed to send data on daily expenses as an alert for those over 5000
"""

import pandas as pd
import pika

# Load CSV data
df = pd.read_csv('DailyExpenses.csv')

# Filter out entries without timestamps
df = df.dropna(subset=['Date'])

# Filter entries with Amount > 5000
df = df[df['Amount'] > 5000]

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='expense_alerts')

# Send timestamped data to the queue with alerts
for _, row in df.iterrows():
    date, category, amount = row['Date'], row['Category'], row['Amount']
    
    message = f"ALERT: Date {date}, Category {category}, Amount {amount} is over 5000!"

    channel.basic_publish(exchange='', routing_key='expense_alerts', body=message)

# Close the connection
connection.close()
#finished!

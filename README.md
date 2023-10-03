# streaming-07-daily-expenses
### Final Project for Streaming Data course

I located a csv file with timestamped data on daily expenses. The file included several columns like category, subcategory of expenses, as well as the amount of the expense. I designed a producer and consumer to send and receive alerts on expenses over $5000 using RabbitMQ. Becuase I was only interested in this one alert, I did not need to use multiple queues.

Some entries included dates, but not a timestamp. For the purposes of this project about streaming data, I excluded these entries through the python code. To similuate streaming, I added a sleep time, but ebcuase I wanted to see if it was working quickly, I set this to just 1.

I had not done the optional assignment of sending an alert to email, so I tackled that this time around. Suggestions from classmates helped me figure out how to us .gitignore and .env to store my password and from_email. I also worked around gmail errors by creating a two step authentification app password.

The result is a simple producer and consumer app similar to existing banking apps that sends an email alert whenever it finds a daily expense of 5000 or more.

Here is the expense alerts queue running in RabbitMQ
![image](https://github.com/ALedgerwood/streaming-07-daily-expenses/assets/111438988/0ddd43b3-f4fe-446d-8581-6f67ff06f79b)

Here is the producer and consumer running is separate terminals indicating email alerts are being sent
![image](https://github.com/ALedgerwood/streaming-07-daily-expenses/assets/111438988/a98d8449-d8ea-419d-998e-b5aff65983c0)

Here are the email alerts in my inbox
![image](https://github.com/ALedgerwood/streaming-07-daily-expenses/assets/111438988/0947f51e-3743-4da2-99d6-0660222a494d)






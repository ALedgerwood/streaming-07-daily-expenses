# streaming-07-daily-expenses
### Final Project for Streaming Data course

I located a csv file with timestamped data on daily expenses. The file included several columns like category, subcategory of expenses, as well as the amount of the expense. I designed a producer and consumer to send and receive alerts on expenses over $5000 using RabbitMQ. Becuase I was only interested in this one alert, I did not need to use multiple queues.

Some entries included dates, but not a timestamp. For the purposes of this project about streaming data, I excluded these entries through the python code. To similuate streaming, I added a sleep time, but ebcuase I wanted to see if it was working quickly, I set this to just 1.

I had not done the optional assignment of sending an alert to email, so I tackled that this time around. Suggestions from classmates helped me figure out how to us .gitignore and .env to store my password and from_email. I also worked around gmail errors by creating a two step authentification app password.

The result is a simple producer and consumer app similar to existing banking apps that sends an email alert whenever it finds a daily expense of 5000 or more.


#
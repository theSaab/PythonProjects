
import smtplib
import ssl
import datetime as dt
import time
import praw


def message_content():
    message = ''
    reddit = praw.Reddit(client_id='GnkLkx5fpFyGQQ',
                         client_secret='czvjzRXxihdPp-oO9s6YKYufhqE', user_agent='saba webscrape')
    hot_posts = reddit.subreddit('Gaming').hot(limit=10)

    for post in hot_posts:
        message += (' ' + str(post.title[:60]) + ',')

    phrase = 'You have sbscribed to this subscription, \
        please send your credit card information to cancel. \
        Here are the top posts in r/Gaming, ' + str(message)
    return phrase


def send_email():
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


word = message_content()
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "saabfats.testing@gmail.com"  # Enter your address
receiver_email = "saba.fathi@emailgmail.info"  # Enter receiver address
password = ''
message = word


start_time = time.time()
seconds = 86400

while True:
    time.sleep(seconds)
    send_email()
    print('email sent, master')



'''
from bs4 import BeautifulSoup
import requests
import pandas as pd
page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
img = tonight.find("img")
desc = img['title']
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc":descs
})
'''
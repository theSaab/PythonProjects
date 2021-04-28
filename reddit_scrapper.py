
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



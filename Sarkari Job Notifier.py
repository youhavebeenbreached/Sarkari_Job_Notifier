import feedparser
from getch import pause
import urllib.request
import time

# Ask to Begin
start = input("Would you like to begin, Sir? (y/n): ")
if start == "y":
    timeLoop = True
else:
    exit()


def connect(host='https://www.google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

if connect():
    print('Connecting........')

else:
    pause('There is no internet connection. Come back when internet connection is available.')
    exit()



url = "https://results.amarujala.com/rss/jobs.xml"

JobFeed = feedparser.parse(url)


print ('************* JOB NOTIFIER *************')



for post in JobFeed.entries:
    print ()
    print ('Job Title :',post.title)
    print ()
    print ('Published :',post.published)
    print ()
    print ('Job Description :',post.description)
    print ()
    print ('Job Link :',post.link)
    print ()
    print ('------------------------------------------------------')

pause('Press Any Key To Exit.')


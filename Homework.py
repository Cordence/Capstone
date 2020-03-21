import requests
import time
import random
import urllib.request

for i in range(10):
    value = random.randrange(0, 52, 1)
    url = 'https://api.thingspeak.com/update?api_key=HQOK5JJYCKBG3OJN&field1='
    url = url + str(value)
    urllib.request.urlopen(url)
    time.sleep(20)

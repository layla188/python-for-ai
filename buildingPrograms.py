def check_weather ():
    temp = 22
    if temp > 23:
        print("it's nice weather")
    else:
        print("it's not a nice weather")

check_weather()

def greet(fname, lname):
    print(f"hello {fname} {lname}")

greet("layla", "yasser")
greet(fname= "lolo", lname= "soso")

def add_item(item, list=None):
    if list is None:
        list = []
    list.append(item)
    return list
add_item(12, [1,2])

def simplw_un():
    nums = [1,2,3,4]
    fnum = nums[0]
    lnum = nums[-1]
    return fnum, lnum
fir, last= simplw_un()
##################################################
# Import entire module
import random

# Use module functions
number = random.randint(1, 10)
choice = random.choice(["apple", "banana", "orange"])

# Date and time
import datetime
time = datetime.datetime.now()
print(time)  # 2024-01-15

import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data)
type(data)
data.keys()
data["current"]["temperature_2m"]

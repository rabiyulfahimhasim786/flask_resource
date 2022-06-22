# Python program to get
# Yesterday's date


# Import date and timedelta class
# from datetime module
from datetime import date
from datetime import timedelta

# Get today's date
today = date.today()
print("Today is: ", today)

# Yesterday date
yesterday = today - timedelta(days = 1)
print("Yesterday was: ", yesterday)

# Define the ticker list
import pandas as pd
import yfinance as yf
# reading a second row in csv
import csv
import os
from datetime import date
from datetime import timedelta

today = date.today()
yesterday = today - timedelta(days = 1)
path = 'test'

# Check whether the specified path exists or not
isExist = os.path.exists(path)

if not isExist:
    # Create a new directory because it does not exist 
    os.makedirs(path)
    print("The new directory is created!")

noise_amp=[]         #an empty list to store the second column
with open('500.csv', 'r') as rf:
    reader = csv.reader(rf, delimiter=',')
    for row in reader:
        noise_amp.append(row[1]) # which row we need to read , 1 is frist row , 2 is second row
    print(noise_amp)

list = noise_amp[498:500]
print(list)

# Define the ticker list
#import pandas as pd
#import yfinance as yf
#list = ['']
for i in list:
  tickers_list = [i]

# Fetch the data
  #import yfinance as yf
  #name = yf.download(tickers_list,'2015-1-1')
  name = yf.download(tickers_list, yesterday)
#data = yf.download(tickers_list,'2015-1-1')
  #name.to_csv('test/{stock}.csv'.format(stock = i))
  name.to_csv('{stock}.csv'.format(stock = i))
# Print first 5 rows of the data
  print(name.head())
#print(data.head())
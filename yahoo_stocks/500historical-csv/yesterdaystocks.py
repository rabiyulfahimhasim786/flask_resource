from flask import Flask, redirect, url_for, request
import pandas as pd
import yfinance as yf
# reading a second row in csv
import csv

import os
from datetime import date
from datetime import timedelta

#today = date.today()
#yesterday = today - timedelta(days = 1)
directory = 'yesterday'
itsExist = os.path.exists(directory)

if not itsExist:
    os.makedirs(directory)
    print("The new directory is created!")

app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
	return 'hello world'

# the associated function.
@app.route('/yesterday', methods = ['GET','POST'])
# ‘/’ URL is bound with hello_world() function.
def yesterday():
    today = date.today()
    yesterday = today - timedelta(days = 1)
    noise_amp=[]         #an empty list to store the second column
    with open('500.csv', 'r') as rf:
        reader = csv.reader(rf, delimiter=',')
        for row in reader:
            noise_amp.append(row[1]) # which row we need to read , 1 is frist row , 2 is second row
        print(noise_amp)

    list = noise_amp[1:500]
    print(list)
    for i in list:
        tickers_list = [i]
        #name = yf.download(tickers_list,'2015-1-1')
        name = yf.download(tickers_list, yesterday)
        name.to_csv('yesterday/{stock}.csv'.format(stock = i))
        print(name.head())
    return 'hello world'

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
	# on the local development server.
	app.run()
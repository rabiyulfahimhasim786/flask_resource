from flask import Flask, request, redirect, render_template, url_for, jsonify, make_response, flash, redirect,url_for,session,logging,request
import yfinance as yf
from decimal import Decimal
# import requests module
import requests
import cffi
from jinja2 import escape
import yfinance as yf
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from df2gspread import df2gspread as d2g
import requests
#import schedule
import pandas as pd
#import time
import optparse
import os
from fake_useragent import UserAgent
#import pyuser_agent
from decimal import Decimal
import json
import schedule
import time
from datetime import datetime, timedelta
app = Flask('app')

@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
  
        data = "hello world"
        return jsonify({'data': data})

#@app.route('/key/<x>', methods = ['GET', 'POST'])
#def key(x):
 #   if(request.method == 'GET'):
 #       #symbol = request.args.get('symbol', x)
 #       getinformation = yf.Ticker(x)
 
# get all key value pairs that are available
  #      for key, value in getinformation.info.items():
  #        data = (key, ":", value)
  #      return data


@app.route('/info/', methods =["GET", "POST"])
def display_quote():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        x = request.form['text']
    
        symbol = request.args.get('symbol', x)

        quote = yf.Ticker(symbol)

        return quote.info
        #return redirect(url_for("datas",  x=x))
    else:
        return render_template("forms.html")

@app.route("/info/<x>", methods =["GET", "POST"])
def datas(x):
    #x = request.form['text']
    symbol = request.args.get('symbol', x)
 
    quote = yf.Ticker(symbol)
    return quote.info




@app.route("/history", methods =["GET", "POST"])
def display_history():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        text = request.form['text']

        symbol = request.args.get('symbol', text)
        period = request.args.get('period', default="1y")
        interval = request.args.get('interval', default="1mo")        
        quote = yf.Ticker(symbol)   
        hist = quote.history(period=period, interval=interval)
        data = hist.to_json()
        return data
    return render_template("history.html")

@app.route("/historydata/<x>")
def history(x):
    #x = request.form['text']
    symbol = request.args.get('symbol', x)
    period = request.args.get('period', default="1y")
    interval = request.args.get('interval', default="1mo")        
    quote = yf.Ticker(symbol)   
    hist = quote.history(period=period, interval=interval)
    data = hist.to_json()
    return data

@app.route("/stockdata", methods =["GET", "POST"])
def display_data():
     if request.method == "POST":
        # getting input with name = fname in HTML form
        text = request.form['text']
        symbol = request.args.get('symbol', text)
        quote = yf.Ticker(symbol)
#start = datetime.datetime(2018,1,1)
#end = datetime.datetime(2019,7,17)
#data = yf.download(stocks, start=start, end=end)
   # a = quote.info['shortName']
    #b = quote.info['symbol']
   # c = quote.info['currentPrice']
   # d = quote.info['profitMargins']
   # e = quote.info['volume']
   # f = quote.info['averageVolume']
   # g = quote.info['marketCap']
    #h = quote.info['trailingPE']
    #i = (a, b, c, d, e, f, g, h)
        return {
   "company_name": quote.info['shortName'],
   "company_symbol": quote.info['symbol'],
   "current_price": quote.info['currentPrice'],
   "profit_margins": quote.info['profitMargins'],
   "volume": quote.info['volume'],
   "average_volume": quote.info['averageVolume'],
   "marketcap": quote.info['marketCap'],
    }
     return render_template("data.html")

@app.route("/stock/<x>")
def invidual(x):
    #x = request.form['text']
    #text = request.form['text']
    symbol = request.args.get('symbol', x)
    quote = yf.Ticker(symbol)
    name = quote.info['shortName']
    symbol = quote.info['symbol']
    price = quote.info['currentPrice']
    margin = quote.info['profitMargins']
    volume = quote.info['volume']
    avg_vloume = quote.info['averageVolume']
    mkt_cap = quote.info['marketCap']
    value = '1'
    #r = requests.get('https://testing.mobilteam.repl.co/stock/amd')
    data = [{
   "company_name": name,
   "company_symbol": symbol,
   "current_price": price,
   "profit_margins": margin,
   "volume": volume,
   "average_volume": avg_vloume,
   "marketcap": mkt_cap,
    }]
    return jsonify({
      'code': value,
      #'status': r.status_code,
      'data': data})


@app.route("/stocks/<x>")
def stock_test(x):
    #x = request.form['text']
    #text = request.form['text']
    symbol = request.args.get('symbol', x)
    quote = yf.Ticker(symbol)
    value = '2'
    a = Decimal(quote.info['currentPrice'])
    b = Decimal(quote.info['previousClose'])
    change = round((a-b), 2)
    # (New Price - Old Price) / Old Price x 100
    d = round((((a-b)/b)*100), 2)
    #r = requests.get('https://testing.mobilteam.repl.co/stock/amd')
    data = [{
   "company_name": quote.info['shortName'],
   "company_symbol": quote.info['symbol'],
   "current_price": quote.info['currentPrice'],
   #"profit-margins": quote.info['profitMargins'],
   "volume": quote.info['volume'],
   "average_volume": quote.info['averageVolume'],
   #"marketcap": quote.info['marketCap'],
   #"52_weeks_company_range_min": quote.info['fiftyTwoWeekLow'],
   #"52_weeks_company_range_max": quote.info['fiftyTwoWeekHigh'],
   #"days_range_min": quote.info['dayLow'],
   #"days_range_max": quote.info['dayHigh'],
   "Previous_close": quote.info['previousClose'],
   "change": change,
   "change_percentage": d,
    }]
    return jsonify({
      'code': value,
      #'status': r.status_code,
      'data': data})

@app.route("/invidual-stock/<x>")
def data_test(x):
    #x = request.form['text']
    #text = request.form['text']
    symbol = request.args.get('symbol', x)
    quote = yf.Ticker(symbol)
    value = '2'
    a = Decimal(quote.info['currentPrice'])
    b = Decimal(quote.info['previousClose'])
    change = round((a-b), 2)
    # (New Price - Old Price) / Old Price x 100
    d = round((((a-b)/b)*100), 2)
    #r = requests.get('https://testing.mobilteam.repl.co/stock/amd')
    data = [{
   "company_name": quote.info['shortName'],
   "company_symbol": quote.info['symbol'],
   "current_price": quote.info['currentPrice'],
   "profit-margins": quote.info['profitMargins'],
   "volume": quote.info['volume'],
   "average_volume": quote.info['averageVolume'],
   "marketcap": quote.info['marketCap'],
   "52_weeks_company_range_min": quote.info['fiftyTwoWeekLow'],
   "52_weeks_company_range_max": quote.info['fiftyTwoWeekHigh'],
   "days_range_min": quote.info['dayLow'],
   "days_range_max": quote.info['dayHigh'],
   "Previous_close": quote.info['previousClose'],
   "change": change,
   "change_percentage": d,
    }]
    return jsonify({
      'code': value,
      #'status': r.status_code,
      'data': data})


@app.route("/gainersfile", methods =["GET", "POST"])
def gainersdatas():
    if request.method == "POST":
        if True:
            url = request.form['text']
            # getting input with name = fname in HTML form
            #ua = pyuser_agent.UA()
            ua = UserAgent()
            #url = request.form['namee']
            #url = 'https://finance.yahoo.com/gainers?count=100&offset=0'
            headers = {'User-Agent': ua.random }
            html = requests.get(url, headers=headers).content
        #html = requests.get(url).content
            soup = BeautifulSoup(html, 'lxml')
            ac = soup.find_all('a', attrs={'data-test': 'quoteLink'})
            bc = soup.find_all('td', attrs={'aria-label': 'Name'})
            cc = soup.find_all('td', attrs={'aria-label': 'Price (Intraday)'})
            dc = soup.find_all('td', attrs={'aria-label': 'Change'})
            ec = soup.find_all('td', attrs={'aria-label': '% Change'})
            fc = soup.find_all('td', attrs={'aria-label': 'Volume'})
            gc = soup.find_all('td', attrs={'aria-label': 'Avg Vol (3 month)'})
            hc = soup.find_all('td', attrs={'aria-label': 'Market Cap'})
            ic = soup.find_all('td', attrs={'aria-label': 'PE Ratio (TTM)'})
  

            ac_ = []
            bc_ = []
            cc_ = []
            dc_ = []
            ec_ = []
            fc_ = []
            gc_ = []
            hc_ = []
            ic_ = []
            for title in ac:
                ac_.append(title.text.strip())
            for title in bc:
                bc_.append(title.text.strip())
            for title in cc:
                cc_.append(title.text.strip())
            for title in dc:
                dc_.append(title.text.strip())
            for title in ec:
                ec_.append(title.text.strip())
            for title in fc:
                fc_.append(title.text.strip())
            for title in gc:
                gc_.append(title.text.strip())
            for title in hc:
                hc_.append(title.text.strip())
            for title in ic:
                ic_.append(title.text.strip())
  # dataframe Name and Age columns
            df = pd.DataFrame({'Symbol': ac_, 'Name': bc_, 'Price': cc_, 'Change': dc_, 'Change %': ec_, 'Volume': fc_, 'Avg volume': gc_, 'Market cap': hc_, 'Ration': ic_,})
            scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']
            creds = ServiceAccountCredentials.from_json_keyfile_name('s.json', scope)
            client = gspread.authorize(creds)
            spreadsheet_key = '1m-mrYAqoUvm5OTN1dq8rRr3sLtDuEh8bxVzQCYi2q44'
            wks_name = 'Sheet1'
            cell_of_start_df = 'A2'
            d2g.upload(df,
            spreadsheet_key,
            wks_name,
            credentials=creds,
            col_names=False,
            row_names=False,
            start_cell = cell_of_start_df,
            clean=False)
            requests.get("https://stocks.desss-portfolio.com/yahoo/yahoo_gainers")
          #  return schedule.CancelJob
            return 'ok'
    #schedule.every(1).seconds.do(gainersdatas)
    #while True:
    #    schedule.run_pending()
    #    if not schedule.jobs:
    #        break
    #    time.sleep(1)
    return render_template("gainers4.html")

  
app.run(host='0.0.0.0', port=8080)
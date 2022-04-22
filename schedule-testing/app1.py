from flask import Flask
import schedule
import requests
import time
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
@app.route('/hello', methods=["GET", "POST"])
def hello():
  #print("I'm working...")
  return 'Hello world!'

#def work():
  #time.sleep(1)
  #requests.get('hrfcreation.blogspot.com/')
  #return job
@app.route('/jobtest', methods=["GET", "POST"])
def job():
  print("I'm working...")
  return 'ok'


schedule.every(5).seconds.until(timedelta(seconds=50)).do(job)
while True:
  schedule.run_pending()
    #schedule.run_pending()
  if not schedule.jobs:
    print("Done")
    break
  

if __name__ == '__main__':
  app.run(debug=True, use_reloader=False)
   # app.run(debug=True)#, use_reloader=False)
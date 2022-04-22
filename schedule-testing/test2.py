import time
import atexit
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

@app.route("/test")
def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))
    return "Welcome Home :) !"

scheduler = BackgroundScheduler()
scheduler.add_job(func=print_date_time, trigger="interval", seconds=60)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


if __name__ == "__main__":
    app.run()
from flask import Flask,render_template
from flask import *
from i2p import i2pconverter
app = Flask(__name__)

import os

path = 'test'

# Check whether the specified path exists or not
isExist = os.path.exists(path)
print('path was exist')

if not isExist:
    # Create a new directory because it does not exist 
    os.makedirs(path)
    print("The new directory is created!")

@app.route('/img2pdf', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/converted', methods = ['GET', 'POST'])
def convert():
    global f1
    fi = request.files['img']
    f1 = fi.filename
    fi.save(f1)
    i2pconverter(f1)
    return render_template('converted.html')

@app.route('/download', methods = ['GET', 'POST'])
def download():
    filename = f1.split('.')[0]+'converted.pdf'
    return send_file(filename,as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
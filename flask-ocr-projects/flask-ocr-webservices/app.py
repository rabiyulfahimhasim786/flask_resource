from flask import Flask, render_template, request
from PIL import Image
app = Flask(__name__)
import pytesseract
import os
path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, 'uploads\\')
#selected_language = ['english', 'germany']
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
# for linux
# pytesseract.pytesseract.tesseract_cmd=r'/usr/bin/tesseract'
#C:\Program Files (x86)\Tesseract-OCR
def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))###, lang=selected_language)
    return text
# from ocr_core import ocr_core
# uncomment the line above, if your Flask fails to get access to your function, or your OCR & Flask are on different scripts

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods = ['GET', 'POST'])
def test():
    return "hello"

@app.route('/hello', methods = ['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('upload.html', msg = 'No file selected')
        file = request.files['file']
        if file.filename == '':
            return render_template('upload.html', msg = 'No file')
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            extracted = ocr_core(file)
            return render_template('upload.html', 
                                    msg = 'OCR completed',
                                    extracted = extracted, 
                                    img_src = UPLOAD_FOLDER + file.filename)
    else:
        return render_template('upload.html')
# https://towardsdatascience.com/implementing-optical-character-recognition-ocr-using-pytesseract-5f42cf62ddcc
if __name__ == '__main__':
    app.run()
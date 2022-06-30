import img2pdf

import os
path = 'test'
    # Check whether the specified path exists or not
isExist = os.path.exists(path)
    # Create a new directory because it does not exist 
if not isExist:
    os.makedirs(path)

def i2pconverter(file):
    pdfname = file.split('.')[0]+'converted'+'.pdf'
    with open(pdfname,'wb') as f:
        f.write(img2pdf.convert(file))
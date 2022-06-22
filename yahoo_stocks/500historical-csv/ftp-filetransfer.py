import ftplib
import os
FTP_HOST = "74.208.51.69"
FTP_USER = "stockftpusr"
FTP_PASS = "T11wz8w_"

ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
ftp.encoding = "utf-8"
ftp.cwd('/assets/yahoo/yahoo_historical/') 

dirFTP = "test"#uploadig folder name 
toFTP = os.listdir(dirFTP)

for filename in toFTP:
    with open(os.path.join(dirFTP,filename), 'rb') as file:  #Here I open the file using it's  full path
        ftp.storbinary(f'STOR {filename}', file)  #Here I store the file in the FTP using only it's name as I intended

ftp.quit()
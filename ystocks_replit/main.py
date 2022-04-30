from jinja2 import escape
from flask import Flask, request, redirect, render_template, url_for, jsonify, make_response, flash, redirect,url_for,session,logging,request
import requests
import random
import yfinance as yf
#import requests
from bs4 import BeautifulSoup
import pandas as pd
import optparse
import os
import schedule
import time
from datetime import datetime, timedelta
import ftplib
app = Flask('app')
#
#
user_agent_list = [
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/99.0.1150.36',
'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Vivaldi/4.3',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Vivaldi/4.3',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
#pravin bro -given
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44',
'Mozilla/5.0 (Mobile; LYF/F90M/LYF-F90M-000-02-21-131117; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0 Waterfox/56.2.7',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.191 Amigo/54.0.2840.191 MRCHROME SOC Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0; Pixel XL Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.0 Mobile Safari/537.36 EdgA/41.1.35.1',
'Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-G925F Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36',
  #what is my browser.com
'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN)',
'Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57',
'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1',
#
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko)',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1',
'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
#
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)',
'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)',
'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
##
#
#github mano given
####
#
#
#
'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36', 
'Mozilla/5.0 (iPad; CPU OS 8_1_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B435 Safari/600.1.4', 
'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240', 
'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; LCJB; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MDDRJS; rv:11.0) like Gecko',
'Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFAPWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; Touch; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; LCJB; rv:11.0) like Gecko',
'Mozilla/5.0 (Linux; U; Android 4.0.3; en-us; KFOT Build/IML74K) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36',
'Mozilla/5.0 (iPad; CPU OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B329 Safari/8536.25', 
'Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFARWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36', 
'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; ASU2JS; rv:11.0) like Gecko', 
'Mozilla/5.0 (iPad; CPU OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A405 Safari/600.1.4',
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', 
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/7.0.5 Safari/537.77.4', 
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36', 
'Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; yie11; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko', 
'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/8.0.57838 Mobile/12H321 Safari/600.1.4', 
'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',
'Mozilla/5.0 (Windows NT 10.0; rv:40.0) Gecko/20100101 Firefox/40.0', 
'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MAGWJS; rv:11.0) like Gecko', 
'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/7.1.5 Safari/537.85.14', 
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko', 
'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; NP06; rv:11.0) like Gecko', 
'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36', 
'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0', 
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174', 
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.4.8 (KHTML, like Gecko) Version/8.0.3 Safari/600.4.8', 
'Mozilla/5.0 (iPad; CPU OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B651 Safari/9537.53', 
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36', 
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.3.18 (KHTML, like Gecko) Version/7.1.3 Safari/537.85.12', 
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko; Google Web Preview) Chrome/27.0.1453 Safari/537.36', 
'Mozilla/5.0 (iPad; CPU OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A365 Safari/600.1.4', 
'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; rv:39.0) Gecko/20100101 Firefox/39.0', 
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4049.US Safari/537.36', 
'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36', 
'Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/45.0.2454.68 Mobile/12H143 Safari/600.1.4',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:38.0) Gecko/20100101 Firefox/38.0', 
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:39.0) Gecko/20100101 Firefox/39.0', 
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H321', 
'Mozilla/5.0 (iPad; CPU OS 7_0_3 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B511 Safari/9537.53', 
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10', 
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36', 
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/7.1.2 Safari/537.85.11', 
'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; ASU2JS; rv:11.0) like Gecko', 
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36',
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.1) Gecko/2008070208 Firefox/3.0.1', 
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0', 
'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MDDCJS; rv:11.0) like Gecko', 
'Mozilla/5.0 (Windows NT 6.3; rv:40.0) Gecko/20100101 Firefox/40.0', 
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.34 (KHTML, like Gecko) Qt/4.8.5 Safari/534.34',
'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53 BingPreview/1.0b',
'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0', 
'Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H143 Safari/600.1.4', 
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36', 
'Mozilla/5.0 (X11; CrOS x86_64 7262.52.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.86 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MDDCJS; rv:11.0) like Gecko', 
'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.4.10 (KHTML, like Gecko) Version/7.1.4 Safari/537.85.13', 
'Mozilla/5.0 (Unknown; Linux x86_64) AppleWebKit/538.1 (KHTML, like Gecko) PhantomJS/2.0.0 Safari/538.1', 
'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MALNJS; rv:11.0) like Gecko', 
'Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/45.0.2454.68 Mobile/12F69 Safari/600.1.4',
'Mozilla/5.0 (Android; Tablet; rv:40.0) Gecko/40.0 Firefox/40.0', 
'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5', 
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', 
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/536.30.1 (KHTML, like Gecko) Version/6.0.5 Safari/536.30.1',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', 
'Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFSAWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36', 
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.104 AOL/9.8 AOLBuild/4346.13.US Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MAAU; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)', 
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36', 
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.74.9 (KHTML, like Gecko) Version/7.0.2 Safari/537.74.9',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', 
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36', 
'Mozilla/5.0 (iPad; CPU OS 7_0_2 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A501 Safari/9537.53',
'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36', 
'Mozilla/5.0 (iPad; CPU OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53',
'Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12F69 Safari/600.1.4', 
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0',
'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MASMJS; rv:11.0) like Gecko', 
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36', 
'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0', 
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174',
'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; FunWebProducts; rv:11.0) like Gecko', 
'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MAARJS; rv:11.0) like Gecko', 
'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUS; rv:11.0) like Gecko',
'Mozilla/5.0 (Linux; Android 4.4.2; SM-T230NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; EIE10;ENUSWOL; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 5.1; rv:39.0) Gecko/20100101 Firefox/39.0', 
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:39.0) Gecko/20100101 Firefox/39.0',
#
]
#
#
#
#url = 'https://httpbin.org/headers'
#for i in range(1,2):
    #Pick a random user agent
    #user_agent = random.choice(user_agent_list)
    #Set the headers 
    #headers = {'User-Agent': user_agent}
  
@app.route('/')
def hello_world():
  return '<h1>Hello, World!</h1>'
  #for i in range(1,2):
    #Pick a random user agent
    #user_agent = random.choice(user_agent_list)
    #print(user_agent)
  #return '<h1>Hello, World!</h1>'

#app.run(host='0.0.0.0', port=8080)


@app.route('/gainerstables', methods=["GET", "POST"])
def gainerstables():
    # converting csv to html
    data = pd.read_csv('yahoo_gainers1.csv')
    return render_template('gainerstable.html', tables=[data.to_html()], titles=[''])


@app.route('/loserstables', methods=["GET", "POST"])
def loserstables():
    # converting csv to html
    data = pd.read_csv('yahoo_losers1.csv')
    return render_template('loserstable.html', tables=[data.to_html()], titles=[''])

@app.route('/mostactivetables', methods=["GET", "POST"])
def mostactivetables():
    # converting csv to html
    data = pd.read_csv('yahoo_most_active1.csv')
    return render_template('mostactivetable.html', tables=[data.to_html()], titles=[''])

@app.route('/trendingtables', methods=["GET", "POST"])
def trendingtables():
    # converting csv to html
    data = pd.read_csv('yahoo_trending1.csv')
    return render_template('trendingtable.html', tables=[data.to_html()], titles=[''])


@app.route("/gainersfile", methods =["GET", "POST"])
def gainersdatas():
    #if request.method == "POST": # use only for post
    if request.method == "GET":
        if True:
            #url = request.form['text']
            # getting input with name = fname in HTML form
            #ua = pyuser_agent.UA()
            #ua = UserAgent()
            url = 'https://finance.yahoo.com/gainers?offset=0&count=100'
            #url = request.form['namee']
            #gainers = form(name = url)
            #db.session.add(gainers)
            #db.session.commit()
            #url = 'https://finance.yahoo.com/gainers?count=100&offset=0'
            for i in range(1,2):
              #Pick a random user agent
              user_agent = random.choice(user_agent_list)
              #headers = {'User-Agent': user_agent }
            print(user_agent) 
            #headers = {'User-Agent': ua.random } # =use only for post
            headers = {'User-Agent': user_agent }
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
    #df = pd.DataFrame({'Symbol': ac_, 'Name': bc_, 'Price': cc_, 'Change': dc_, 'Change %': ec_, 'Volume': fc_, 'Avg volume': gc_, 'Market cap': hc_, 'Ration': ic_,})
            dict = {'Symbol': ac_, 'Name': bc_, 'Price': cc_, 'Change': dc_, 'Change %': ec_, 'Volume': fc_, 'Avg volume': gc_, 'Market cap': hc_, 'Ration': ic_,}
            df = pd.DataFrame(dict)
             # saving the dataframe
            df.to_csv('yahoo_gainers1.csv')
            # Fill Required Information
            HOSTNAME = "74.208.51.69"
            USERNAME = "stockftpusr"
            PASSWORD = "T11wz8w_"
            #Connect FTP Server
            ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
            #ftp_server.login()
            # force UTF-8 encoding
            ftp_server.encoding = "utf-8"
            #ftp_server.cwd changing required directory
            ftp_server.cwd('/assets/yahoo/yahoo_gainers/')
            # Enter File Name with Extension
            filename = "yahoo_gainers1.csv"
            # Read file in binary mode
            with open(filename, "rb") as file:
              # Command for Uploading the file "STOR filename"
              ftp_server.storbinary(f"STOR {filename}", file) 
            # Get list of files
            ftp_server.dir()
            # Close the Connection
            ftp_server.quit()
            requests.get("https://stocks.desss-portfolio.com/yahoo/yahoo_gainers") #schedule.every(10).minutes.until(timedelta(hours=1)).do(gainersdatas)
        #time.sleep(650)
        #requests.get("https://stocks.desss-portfolio.com/yahoo/yahoo_gainers")
            #while 1:
            #  schedule.run_pending()
           #   #time.sleep(1)
           #   if not schedule.jobs:
           #     break
      #time.sleep(1)
        return '200 Status:ok'
        #return 'ok'
    #return render_template("gainersfile.html") use only for post 



@app.route("/gainersdatafile", methods =["GET", "POST"])
def gainersdatafile():
    #if request.method == "POST": # use only for post
    if request.method == "GET":
        if True:
            #url = request.form['text']
            # getting input with name = fname in HTML form
            #ua = pyuser_agent.UA()
            #ua = UserAgent()
            for i in range(1,2):
              #Pick a random user agent
              user_agent = random.choice(user_agent_list)
              #headers = {'User-Agent': user_agent }
            print(user_agent) 
            url = 'https://finance.yahoo.com/gainers?offset=0&count=100'
            #url = request.form['namee']
            #gainers = form(name = url)
            #db.session.add(gainers)
            #db.session.commit()
            #url = 'https://finance.yahoo.com/gainers?count=100&offset=0'
            #headers = {'User-Agent': ua.random } # =use only for post
            headers = {'User-Agent': user_agent }
            html = requests.get(url, headers=headers).content
             #html = requests.get(url).content
            soup = BeautifulSoup(html, 'lxml')
            ab = soup.find_all('a', attrs={'data-test': 'quoteLink'})
            bb = soup.find_all('td', attrs={'aria-label': 'Name'})
            cb = soup.find_all('td', attrs={'aria-label': 'Price (Intraday)'})
            db = soup.find_all('td', attrs={'aria-label': 'Change'})
            eb = soup.find_all('td', attrs={'aria-label': '% Change'})
            fb = soup.find_all('td', attrs={'aria-label': 'Volume'})
            gb = soup.find_all('td', attrs={'aria-label': 'Avg Vol (3 month)'})
            hb = soup.find_all('td', attrs={'aria-label': 'Market Cap'}) 
            ib = soup.find_all('td', attrs={'aria-label': 'PE Ratio (TTM)'})
  

            ab_ = []
            bb_ = []
            cb_ = []
            db_ = []
            eb_ = []
            fb_ = []
            gb_ = []
            hb_ = []
            ib_ = []
            for title in ab:
               ab_.append(title.text.strip())
            for title in bb:
               bb_.append(title.text.strip())
            for title in cb:
              cb_.append(title.text.strip())
            for title in db:
               db_.append(title.text.strip())
            for title in eb:
               eb_.append(title.text.strip())
            for title in fb:
               fb_.append(title.text.strip())
            for title in gb:
              gb_.append(title.text.strip())
            for title in hb:
              hb_.append(title.text.strip())
            for title in ib:
              ib_.append(title.text.strip())
            # dataframe Name and Age columns
    #df = pd.DataFrame({'Symbol': ac_, 'Name': bc_, 'Price': cc_, 'Change': dc_, 'Change %': ec_, 'Volume': fc_, 'Avg volume': gc_, 'Market cap': hc_, 'Ration': ic_,})
            dict = {'Symbol': ab_, 'Name': bb_, 'Price': cb_, 'Change': db_, 'Change %': eb_, 'Volume': fb_, 'Avg volume': gb_, 'Market cap': hb_, 'Ration': ib_,}
            df = pd.DataFrame(dict)
             # saving the dataframe
            df.to_csv('yahoo_gainers2.csv')
            #url = request.form['namee']
            #gainers = form(name = url)
            #db.session.add(gainers)
            #db.session.commit()
            #url = 'https://finance.yahoo.com/gainers?count=100&offset=0'
            #headers = {'User-Agent': ua.random } # =use only for post
            # Fill Required Information
            HOSTNAME = "74.208.51.69"
            USERNAME = "stockftpusr"
            PASSWORD = "T11wz8w_"
            #Connect FTP Server
            ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
            #ftp_server.login()
            # force UTF-8 encoding
            ftp_server.encoding = "utf-8"
            #ftp_server.cwd changing required directory
            ftp_server.cwd('/assets/yahoo/yahoo_gainers/')
            # Enter File Name with Extension
            filename = "yahoo_gainers2.csv"
            #Read file in binary mode
            with open(filename, "rb") as file:
              # Command for Uploading the file "STOR filename"
              ftp_server.storbinary(f"STOR {filename}", file) 
            # Get list of files
            ftp_server.dir()
            # Close the Connection
            # ftp_server.quit()
            #requests.get("https://stocks.desss-portfolio.com/yahoo/yahoo_gainers") #schedule.every(10).minutes.until(timedelta(hours=1)).do(gainersdatas)
        #time.sleep(650)
        #requests.get("https://stocks.desss-portfolio.com/yahoo/yahoo_gainers")
            #while 1:
            #  schedule.run_pending()
           #   #time.sleep(1)
           #   if not schedule.jobs:
           #     break
      #time.sleep(1)
        return '200 Status:ok'
        #return 'ok'
    #return render_template("gainersfile.html") use only for post 


@app.route("/losersfile", methods =["GET", "POST"])
def losersdatasfile():
    if request.method == "GET":
        if True:
            #url = request.form['text']
            # getting input with name = fname in HTML form
            #ua = pyuser_agent.UA()
            #ua = UserAgent()
            url = 'https://finance.yahoo.com/losers?offset=0&count=100'
            #url = request.form['namee']
            #losers = form(name = url)
            #db.session.add(losers)
            #db.session.commit()
            #url = 'https://finance.yahoo.com/gainers?count=100&offset=0'
            for i in range(1,2):
              #Pick a random user agent
              user_agent = random.choice(user_agent_list)
              #headers = {'User-Agent': user_agent }
            print(user_agent) 
            #headers = {'User-Agent': ua.random }
            headers = {'User-Agent': user_agent }
            html = requests.get(url, headers=headers).content
        #html = requests.get(url).content
            soup = BeautifulSoup(html, 'lxml')
            ar = soup.find_all('a', attrs={'data-test': 'quoteLink'})
            br = soup.find_all('td', attrs={'aria-label': 'Name'})
            cr = soup.find_all('td', attrs={'aria-label': 'Price (Intraday)'})
            dr = soup.find_all('td', attrs={'aria-label': 'Change'})
            er = soup.find_all('td', attrs={'aria-label': '% Change'})
            fr = soup.find_all('td', attrs={'aria-label': 'Volume'})
            gr = soup.find_all('td', attrs={'aria-label': 'Avg Vol (3 month)'})
            hr = soup.find_all('td', attrs={'aria-label': 'Market Cap'})
            ir = soup.find_all('td', attrs={'aria-label': 'PE Ratio (TTM)'})
  

            ar_ = []
            br_ = []
            cr_ = []
            dr_ = []
            er_ = []
            fr_ = []
            gr_ = []
            hr_ = []
            ir_ = []
            for title in ar:
                ar_.append(title.text.strip())
            for title in br:
                br_.append(title.text.strip())
            for title in cr:
                cr_.append(title.text.strip())
            for title in dr:
                dr_.append(title.text.strip())
            for title in er:
                er_.append(title.text.strip())
            for title in fr:
                fr_.append(title.text.strip())
            for title in gr:
                gr_.append(title.text.strip())
            for title in hr:
                hr_.append(title.text.strip())
            for title in ir:
                ir_.append(title.text.strip())
  # dataframe Name and Age columns
            dict = {'Symbol': ar_, 'Name': br_, 'Price': cr_, 'Change': dr_, 'Change %': er_, 'Volume': fr_, 'Avg volume': gr_, 'Market cap': hr_, 'Ration': ir_,}
            df = pd.DataFrame(dict)
             # saving the dataframe
            df.to_csv('yahoo_losers1.csv')
            # Fill Required Information
            HOSTNAME = "74.208.51.69"
            USERNAME = "stockftpusr"
            PASSWORD = "T11wz8w_"
            #Connect FTP Server
            ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
            #ftp_server.login()
            # force UTF-8 encoding
            ftp_server.encoding = "utf-8"
            #ftp_server.cwd changing required directory
            ftp_server.cwd('/assets/yahoo/yahoo_losers/')
            # Enter File Name with Extension
            filename = "yahoo_losers1.csv"
            # Read file in binary mode
            with open(filename, "rb") as file:
              # Command for Uploading the file "STOR filename"
              ftp_server.storbinary(f"STOR {filename}", file) 
            # Get list of files
            ftp_server.dir()
            # Close the Connection
            ftp_server.quit()
            requests.get("https://stocks.desss-portfolio.com/yahoo/yahoo_losers")
          #losersfile
        return 'ok'
    #return render_template("losersfile.html")
            #df = pd.DataFrame({'Symbol': ar_, 'Name': br_, 'Price': cr_, 'Change': dr_, 'Change %': er_, 'Volume': fr_, 'Avg volume': gr_, 'Market cap': hr_, 'Ration': ir_,})
            #scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']
           # creds = ServiceAccountCredentials.from_json_keyfile_name('yahoo_losers.json', scope)
            #client = gspread.authorize(creds)
            #spreadsheet_key = '1X7APg9YH6ndu2lEhYDjMrWGwE1mQZlIh3G-XbzV_8zA'
            #wks_name = 'Sheet1'
            #cell_of_start_df = 'A2'
            #d2g.upload(df,
            #spreadsheet_key,
            #wks_name,
            #credentials=creds,
            #col_names=False,
            #row_names=False,
            #start_cell = cell_of_start_df,
            #clean=False)
            #requests.get("https://stocks.desss-portfolio.com/yahoo/yahoo_losers")
          #  return schedule.CancelJob
            
            #return 'ok'
    #schedule.every(1).seconds.do(gainersdatas)
    #while True:
    #    schedule.run_pending()
    #    if not schedule.jobs:
    #        break
    #    time.sleep(1)
    #return render_template("losersfile.html")
    #return make_response(render_template('gainers4.html'),200)
    #else:
       # return render_template("gainers4.html")

#


@app.route("/mostactivefile", methods =["GET", "POST"])
def mostactivefile():
    #if request.method == "POST":
    if request.method == "GET":
        if True:
            #url = request.form['text']
            # getting input with name = fname in HTML form
           # ua = pyuser_agent.UA()
            #ua = UserAgent()
            url = 'https://finance.yahoo.com/most-active?count=100&guce_referrer=aHR0cHM6Ly9sb2dpbi55YWhvby5jb20v&guce_referrer_sig=AQAAAI9gecImEAchRGLbJWaMQRr0edvgHEKjXhV89uZ46DDqOZKQJn7TsZ4k2hHgl09_vQ3_lYa9k_RWrl-tXRFFIR5zhJ5V0CV59JLQKHGfoDQtb_2cD9RLko43tSWYaqR1DtLibvUkwYkJM5MU71P6bpx7nrUwMbOurSz3MmHf7Qey&offset=0'
            #url = request.form['namee']
            #losers = form(name = url)
            #db.session.add(losers)
            #db.session.commit()
            #url = 'https://finance.yahoo.com/gainers?count=100&offset=0'
            for i in range(1,2):
              #Pick a random user agent
              user_agent = random.choice(user_agent_list)
              #headers = {'User-Agent': user_agent }
            print(user_agent) 
            #headers = {'User-Agent': ua.random }
            headers = {'User-Agent': user_agent }
            html = requests.get(url, headers=headers).content
        #html = requests.get(url).content
            soup = BeautifulSoup(html, 'lxml')
            at = soup.find_all('a', attrs={'data-test': 'quoteLink'})
            bt = soup.find_all('td', attrs={'aria-label': 'Name'})
            ct = soup.find_all('td', attrs={'aria-label': 'Price (Intraday)'})
            dt = soup.find_all('td', attrs={'aria-label': 'Change'})
            et = soup.find_all('td', attrs={'aria-label': '% Change'})
            ft = soup.find_all('td', attrs={'aria-label': 'Volume'})
            gt = soup.find_all('td', attrs={'aria-label': 'Avg Vol (3 month)'})
            ht = soup.find_all('td', attrs={'aria-label': 'Market Cap'})
            it = soup.find_all('td', attrs={'aria-label': 'PE Ratio (TTM)'})
  

            at_ = []
            bt_ = []
            ct_ = []
            dt_ = []
            et_ = []
            ft_ = []
            gt_ = []
            ht_ = []
            it_ = []
            for title in at:
                at_.append(title.text.strip())
            for title in bt:
                bt_.append(title.text.strip())
            for title in ct:
                ct_.append(title.text.strip())
            for title in dt:
                dt_.append(title.text.strip())
            for title in et:
                et_.append(title.text.strip())
            for title in ft:
                ft_.append(title.text.strip())
            for title in gt:
                gt_.append(title.text.strip())
            for title in ht:
                ht_.append(title.text.strip())
            for title in it:
                it_.append(title.text.strip())
  # dataframe Name and Age columns

            dict = {'Symbol': at_, 'Name': bt_, 'Price': ct_, 'Change': dt_, 'Change %': et_, 'Volume': ft_, 'Avg volume': gt_, 'Market cap': ht_, 'Ration': it_,}
            df = pd.DataFrame(dict)
             # saving the dataframe
            df.to_csv('yahoo_most_active1.csv')
            # Fill Required Information
            HOSTNAME = "74.208.51.69"
            USERNAME = "stockftpusr"
            PASSWORD = "T11wz8w_"
            #Connect FTP Server
            ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
            #ftp_server.login()
            # force UTF-8 encoding
            ftp_server.encoding = "utf-8"
            #ftp_server.cwd changing required directory
            ftp_server.cwd('/assets/yahoo/most_active/')
            # Enter File Name with Extension
            filename = "yahoo_most_active1.csv"
            # Read file in binary mode
            with open(filename, "rb") as file:
              # Command for Uploading the file "STOR filename"
              ftp_server.storbinary(f"STOR {filename}", file) 
            # Get list of files
            ftp_server.dir()
            # Close the Connection
            ftp_server.quit()
            requests.get("https://stocks.desss-portfolio.com/yahoo/most_active")
          #losersfile
        return 'ok'
    #return render_template("mostactivefiles.html")
            #df = pd.DataFrame({'Symbol': at_, 'Name': bt_, 'Price': ct_, 'Change': dt_, 'Change %': et_, 'Volume': ft_, 'Avg volume': gt_, 'Market cap': ht_, 'Ration': it_,})
            #scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']
            #creds = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
           # client = gspread.authorize(creds)
           # spreadsheet_key = '1hVc3A_XjDt4zYwtEb5YEzQbyyjCn7LcPOQlx03dsHvs'
          #  wks_name = 'Sheet1'
          #  cell_of_start_df = 'A2'
          #  d2g.upload(df,
          #  spreadsheet_key,
          #  wks_name,
         #   credentials=creds,
         #   col_names=False,
         #   row_names=False,
         #   start_cell = cell_of_start_df,
          #  clean=False)
          #  requests.get("https://stocks.desss-portfolio.com/yahoo/most_active")
          #  return schedule.CancelJob
         #   return 'ok'
    #schedule.every(1).seconds.do(gainersdatas)
    #while True:
    #    schedule.run_pending()
    #    if not schedule.jobs:
    #        break
    #    time.sleep(1)
   # return render_template("mostactive4.html")
    #return make_response(render_template('gainers4.html'),200)
    #else:
       # return render_template("gainers4.html")

@app.route("/trendingfile", methods =["GET", "POST"])
def trendingfile():
    #if request.method == "POST":
    if request.method == "GET":
        if True:
            #url = request.form['text']
            # getting input with name = fname in HTML form
            #ua = pyuser_agent.UA()
            #ua = UserAgent()
            url = 'https://finance.yahoo.com/trending-tickers'
            #url = request.form['namee']
            #trending = form(name = url)
            #db.session.add(trending)
            #db.session.commit()
            #url = 'https://finance.yahoo.com/gainers?count=100&offset=0'
            for i in range(1,2):
              #Pick a random user agent
              user_agent = random.choice(user_agent_list)
              #headers = {'User-Agent': user_agent }
            print(user_agent) 
           # headers = {'User-Agent': ua.random }
            headers = {'User-Agent': user_agent }
            html = requests.get(url, headers=headers).content
        #html = requests.get(url).content
            soup = BeautifulSoup(html, 'lxml')

            au = soup.find_all('a', attrs={'class': 'Fw(600) C($linkColor)'})
            bu = soup.find_all('td', attrs={'aria-label': 'Name'})
            cu = soup.find_all('td', attrs={'aria-label': 'Last Price'})
            du = soup.find_all('td', attrs={'aria-label': 'Market Time'})
            eu = soup.find_all('td', attrs={'aria-label': 'Change'})
            fu = soup.find_all('td', attrs={'aria-label': '% Change'})
            gu = soup.find_all('td', attrs={'aria-label': 'Volume'})
            hu = soup.find_all('td', attrs={'aria-label': 'Market Cap'})
  

            au_ = []
            bu_ = []
            cu_ = []
            du_ = []
            eu_ = []
            fu_ = []
            gu_ = []
            hu_ = []
            for title in au:
                au_.append(title.text.strip())
            for title in bu:
                bu_.append(title.text.strip())
            for title in cu:
                cu_.append(title.text.strip())
            for title in du:
                du_.append(title.text.strip())
            for title in eu:
                eu_.append(title.text.strip())
            for title in fu:
                fu_.append(title.text.strip())
            for title in gu:
                gu_.append(title.text.strip())
            for title in hu:
                hu_.append(title.text.strip())
            dict = {'Symbol': au_, 'Name': bu_, 'Price': cu_, 'Market Time': du_, 'Change': eu_, 'Change %': fu_, 'Volume': gu_, 'Market cap': hu_}
            df = pd.DataFrame(dict)
             # saving the dataframe
            df.to_csv('yahoo_trending1.csv')
            # Fill Required Information
            HOSTNAME = "74.208.51.69"
            USERNAME = "stockftpusr"
            PASSWORD = "T11wz8w_"
            #Connect FTP Server
            ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
            #ftp_server.login()
            # force UTF-8 encoding
            ftp_server.encoding = "utf-8"
            #ftp_server.cwd changing required directory
            ftp_server.cwd('/assets/yahoo/yahoo_trending/')
            # Enter File Name with Extension
            filename = "yahoo_trending1.csv"
            # Read file in binary mode
            with open(filename, "rb") as file:
              # Command for Uploading the file "STOR filename"
              ftp_server.storbinary(f"STOR {filename}", file) 
            # Get list of files
            ftp_server.dir()
            # Close the Connection
            ftp_server.quit()
            requests.get("https://stocks.desss-portfolio.com/yahoo/yahoo_trending")
          #losersfile
        return 'ok'
    #return render_template("trendingfiles.html") 
              # dataframe Name and Age columns
           # df = pd.DataFrame({'Symbol': au_, 'Name': bu_, 'Price': cu_, 'Market Time': du_, 'Change': eu_, 'Change %': fu_, 'Volume': gu_, 'Market cap': hu_})
           
          # scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']
           # creds = ServiceAccountCredentials.from_json_keyfile_name('yahoo_trendings.json', scope)
           # client = gspread.authorize(creds)
            #spreadsheet_key = '1FDbwLYGQHiuVALZBUcId-OggbZxdrO4CJGncd0zoY0Q'
            #wks_name = 'Sheet1'
           # cell_of_start_df = 'A2'
           # d2g.upload(df,
           # spreadsheet_key,
           # wks_name,
           # credentials=creds,
           # col_names=False,
           # row_names=False,
           # start_cell = cell_of_start_df,
           # clean=False)
           # requests.get("https://stocks.desss-portfolio.com/yahoo/yahoo_trending")
          #  return schedule.CancelJob
           # return 'ok'
    #schedule.every(1).seconds.do(gainersdatas)
    #while True:
    #    schedule.run_pending()
    #    if not schedule.jobs:
    #        break
    #    time.sleep(1)
    #return render_template("trending4.html")
    #return make_response(render_template('gainers4.html'),200)
    #else:
       # return render_template("gainers4.html")

#
#
      #

@app.route("/nasdaqc", methods =["GET", "POST"])
def nasdaqc():
    #if request.method == "POST":
    if request.method == "GET":
        if True:
            for i in range(1,2):
                #Pick a random user agent
                user_agent = random.choice(user_agent_list)
            #headers = {'User-Agent': user_agent }
            #print(user_agent)
            url = 'https://finance.yahoo.com/quote/%5EIXIC'

            headers = {'User-Agent': user_agent }
            print(user_agent)
            html = requests.get(url, headers=headers).content
            #html = requests.get(url).content
            soup = BeautifulSoup(html, 'lxml')
            price = soup.find_all('fin-streamer', attrs={'data-test': 'qsp-price'})
            previousclose = soup.find_all('td', attrs={'data-test': 'PREV_CLOSE-value'})
            change = soup.find_all('fin-streamer', attrs={'data-test': 'qsp-price-change'})
            fiftytwo = soup.find_all('td', attrs={'data-test': 'FIFTY_TWO_WK_RANGE-value'})
            day = soup.find_all('td', attrs={'data-test': 'DAYS_RANGE-value'})

            price_ = []
            previousclose_ = []
            change_ = []
            fiftytwo_ = []
            day_ = []

            for title in price:
                price_.append(title.text.strip())
            for title in previousclose:
                previousclose_.append(title.text.strip())
            for title in change:
                change_.append(title.text.strip())
            for title in fiftytwo:
                fiftytwo_.append(title.text.strip())
            for title in day:
                day_.append(title.text.strip())
            #
            dictionary = {'Price': price_, 'Previousclose': previousclose_, 'Change': change_, 'Fiftytwo': fiftytwo_, 'Day': day_,} #'Fiftytwo': fiftytwo_, }#'Volume': fb_, 'Avg volume': gb_, 'Market cap': hb_, 'Ration': ib_,}
            df = pd.DataFrame(dictionary)
            # saving the dataframe
            df.to_csv('yahoo_nasdaq_current.csv')
            # Fill Required Information
            HOSTNAME = "74.208.51.69"
            USERNAME = "stockftpusr"
            PASSWORD = "T11wz8w_"
            #Connect FTP Server
            ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
            #ftp_server.login()
            # force UTF-8 encoding
            ftp_server.encoding = "utf-8"
            #ftp_server.cwd changing required directory
            ftp_server.cwd('/assets/yahoo/yahoo_global/')
            # Enter File Name with Extension
            filename = "yahoo_nasdaq_current.csv"
            # Read file in binary mode
            with open(filename, "rb") as file:
              # Command for Uploading the file "STOR filename"
              ftp_server.storbinary(f"STOR {filename}", file) 
            # Get list of files
            ftp_server.dir()
            # Close the Connection
            ftp_server.quit()
            requests.get("https://stocks.desss-portfolio.com/yahoo/yahoo_global_current")
          #losersfile
        return 'ok'
###
      ###
###
####
@app.route("/nasdaqfuture", methods =["GET", "POST"])
def nasdaqfuture():
    #if request.method == "POST":
    if request.method == "GET":
        if True:
            for i in range(1,2):
                #Pick a random user agent
                user_agent = random.choice(user_agent_list)
            #headers = {'User-Agent': user_agent }
            #print(user_agent)
            url = 'https://finance.yahoo.com/quote/NQ%3DF?p=NQ%3DF'
            headers = {'User-Agent': user_agent }
            print(user_agent)
            html = requests.get(url, headers=headers).content
            #html = requests.get(url).content
            soup = BeautifulSoup(html, 'lxml')
            nfutureprice = soup.find_all('fin-streamer', attrs={'data-test': 'qsp-price'})
            changes = soup.find_all('fin-streamer', attrs={'data-test': 'qsp-price-change'})
            lastprice = soup.find_all('td', attrs={'data-test': 'LAST_PRICE-value'})


            futureprice_ = []
            changes_ = []
            lastprice_ = []

            for title in nfutureprice:
                futureprice_.append(title.text.strip())
            for title in changes:
                changes_.append(title.text.strip())
            for title in lastprice:
                lastprice_.append(title.text.strip())
            dictionary = {'Price': futureprice_, 'Change': changes_, 'previous close': lastprice_}
            df = pd.DataFrame(dictionary)
             # saving the dataframe
            df.to_csv('yahoo_nasdaq_future.csv')
            #print(user_agent)
            # Fill Required Information
            HOSTNAME = "74.208.51.69"
            USERNAME = "stockftpusr"
            PASSWORD = "T11wz8w_"
            #Connect FTP Server
            ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
            #ftp_server.login()
            # force UTF-8 encoding
            ftp_server.encoding = "utf-8"
            #ftp_server.cwd changing required directory
            ftp_server.cwd('/assets/yahoo/yahoo_global/')
            # Enter File Name with Extension
            filename = "yahoo_nasdaq_future.csv"
            # Read file in binary mode
            with open(filename, "rb") as file:
              # Command for Uploading the file "STOR filename"
              ftp_server.storbinary(f"STOR {filename}", file) 
            # Get list of files
            ftp_server.dir()
            # Close the Connection
            ftp_server.quit()
            requests.get("https://stocks.desss-portfolio.com/yahoo/yahoo_global_future")
          #losersfile
        return 'ok'
####
      ###
app.run(host='0.0.0.0', port=8080)
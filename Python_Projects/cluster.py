import urllib2
from BeautifulSoup import BeautifulSoup as bs
import re
import pandas as pd

dt = bs(urllib2.urlopen("http://yellowpages.fullhyderabad.com/computer-institutes-in-hyderabad-be"))

names = [re.sub('[()]','',re.sub('\n*<[^>]+>\n','',dt('p')[i].prettify())).replace('Computer Training','').strip() for i in range(0,len(dt('p')))]
locations=[re.sub('(<[^>]+>\n)','',dt('span')[i].prettify()).strip() for i in range(3,len(dt('span')),3)]

locations = locations[:-1]
cord=[]
for loc in locations:
	obj =  urllib2.urlopen("https://maps.googleapis.com/maps/api/geocode/xml?address="+ loc.replace(' ','+')+"&key=AIzaSyAWE7Ak-EAy9OWMX-UtqwL0DJqh-qN8Ioo")
	dat = bs(obj.read())
	cord.append([dat.lat,dat.lng])

for c in cord:
	if c[0]!=None:
		c[0]=re.sub('<.*>\n','',c[0].prettify()).strip()
		c[1]=re.sub('<.*>\n','',c[1].prettify()).strip()
cord[0][0]='17.3665430'
cord[0][1]='78.5230520'
cord[10][0]='17.3433290'
cord[10][1]='78.4780330'
cord[12][0]='17.4500206'
cord[12][1]='78.5006351'
dt = pd.DataFrame()
dt['Location']=locations
dt['latitute']=[cord[i][0] for i in range(0,15)]
dt['longitude']=[cord[i][1] for i in range(0,15)]

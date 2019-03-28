
import csv
import requests
import datetime


def getData(year,month,from1,to,statio):
    url = "http://weather.uwyo.edu/cgi-bin/sounding?region=seasia&TYPE=TEXT%3ARAW&YEAR="+year+"&MONTH="+month+"&FROM="+from1+"&TO="+to+"&STNM="+station
    
    response = requests.get(url)
    response = str(response.content)
    response = response[3:]
    first = response.split("TTBB")
    second = first[1].split("TTCC")
    TTCC = second[1]
    TTBB = second[0]
    TTAA = first[0]
    TTAA = TTAA.replace('\\n'," ")
    TTAA = TTAA.replace("TTAA","")
    TTBB = TTBB.replace("\\n"," ")
    TTCC = TTCC.replace("\\n"," ")
    lines = []
    name = "wyomingData/"
    name += statio+".csv"
    with open(name, 'a') as csvFile:
        writer = csv.writer(csvFile)
        now = datetime.datetime.now()
        row = [TTAA, TTBB, TTCC,now]
        writer.writerow(row)

year = "2019"
month = "3"
from1 = "2800"
to = "2800"
stationCodes = ['42182']
# ,'42101','42182','42339','42361','42379','42299','42314']
for station in stationCodes:
    getData(year,month,from1,to,station)

import csv
import sys
import os
import urllib, json
import time


latitude=2
longitude=3
TruckID = 4

geo_dir =os.path.dirname('C:\Users\Dario\Desktop\ ') #os.path.dirname('D:\Tesi\\raw data\crescini\ ')

with open(geo_dir+'\cresciniErrors.csv','rb') as geo:

    reader = csv.reader(geo)
    next(reader,None)
    geow =open(geo_dir+'\erroriProva25.csv','wt')
    writer = csv.writer(geow, lineterminator='\n')
    writer.writerow(('n','ID','Lat','Long','TruckID','TruckCo2Warning','TruckCo2Value','GenerationDate','TimeStamp','TruckMileage','MarkDeleted','Speed','HDOP','FirmeWareVersion','Error','address','type','importance'))
    for row in reader:


        time.sleep(1)
        lat=row[latitude]
        lon=row[longitude]
        print(lat, lon)
        try:
            url = 'http://nominatim.openstreetmap.org/search.php?format=json&q=' + lat + '%2C' + lon + '&polygon=1&viewbox='
            response = urllib.urlopen(url)
            data = json.loads(response.read())
            print (data[0]['display_name'] )
            row.append(data[0]['display_name'].encode('utf-8'))
            row.append(data[0]['type'])
            row.append(data[0]['importance'])

            print(row)
            writer.writerow((row))
        except:
            writer.writerow((row,"error"))



    geo.close()
    geow.close()




import urllib.request
import os
import time

path = "./data/intraQuarter"

def Check_Yahoo():

    statspath = path+'/_KeyStats/'

    # folders of companies
    stock_list = [x[0] for x in os.walk(statspath)]

    for e in stock_list[1:]:
        try:
            e = e.replace(statspath,"")
            link = "http://finance.yahoo.com/q/ks?s="+e.upper()+"+Key+Statistics"
            resp = urllib.request.urlopen(link).read()

            fileName = "data/yahooReq/"+str(e)+".html"
            fileWriter = open(fileName,"w")
            fileWriter.write(str(resp))
            fileWriter.close()

        except Exception as e:
            print(str(e))
            time.sleep(2)

Check_Yahoo()

import pandas as pd
import os
from Quandl import Quandl
import time



auth_tok = open("./data/auth.txt","r").read()
path = "./data/intraQuarter"


def Stock_Prices():
	df =pd.DataFrame()
	statspath = path+'/_KeyStats'

	# Start time
	start_time = time.time()

	# folders of companies
	stock_list = [x[0] for x in os.walk(statspath)]
	for each_dir in stock_list[1:]:
		try:
			ticker = each_dir.split(statspath+'/')[1]
			print('firstTry: ',ticker)
			name="WIKI/"+ticker.upper()
			data = Quandl.get(	name,
								authtoken=auth_tok,
								trim_start='2000-12-12',
								trim_end='2014-12-30')

			data[ticker.upper()] = data["Adj. Close"]
			df = pd.concat([df,data[ticker.upper()]],axis = 1
				)
		except Exception as e:
			print(str(e))
			# time.sleep(10)
			try:
				ticker = each_dir.split('/')[1]
				print('secondTry: ',ticker)
				name="WIKI/"+ticker.upper()
				data = Quandl.get(	name,
									authtoken=auth_tok,
									trim_start='2000-12-12',
									trim_end='2014-12-30')

				data[ticker.upper()] = data["Adj. Close"]
				df = pd.concat([df,data[ticker.upper()]],axis = 1
					)
			except Exception as e:
				print(str(e))
	df.to_csv("./data/stock_prices.csv")
	print("--- %s seconds ---" % (time.time() - start_time))
	print ("stock_prices.csv is done.")

Stock_Prices()
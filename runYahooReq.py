import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, preprocessing
import pandas as pd
from matplotlib import style
import statistics

style.use("ggplot")

def fileToSave(withNA,enhanced,fileName):

	fileName = fileName
	if withNA == True:
		fileName += "_WITH_NA"
	else:
		fileName += "_NO_NA"

	if enhanced == True:
		fileName +="_enhanced"

	fileName +=".csv"
	print("using: ",fileName)
	return fileName

FEATURES =  ['DE Ratio',
			 'Trailing P/E',
			 'Price/Sales',
			 'Price/Book',
			 'Profit Margin',
			 'Operating Margin',
			 'Return on Assets',
			 'Return on Equity',
			 'Revenue Per Share',
			 'Market Cap',
			 'Enterprise Value',
			 'Forward P/E',
			 'PEG Ratio',
			 'Enterprise Value/Revenue',
			 'Enterprise Value/EBITDA',
			 'Revenue',
			 'Gross Profit',
			 'EBITDA',
			 'Net Income Avl to Common ',
			 'Diluted EPS',
			 'Earnings Growth',
			 'Revenue Growth',
			 'Total Cash',
			 'Total Cash Per Share',
			 'Total Debt',
			 'Current Ratio',
			 'Book Value Per Share',
			 'Cash Flow',
			 'Beta',
			 'Held by Insiders',
			 'Held by Institutions',
			 'Shares Short (as of',
			 'Short Ratio',
			 'Short % of Float',
			 'Shares Short (prior ']

def Build_Data_Set(withNA,enhanced):
	data_df = pd.DataFrame.from_csv("./data/"+fileToSave(withNA,enhanced,"key_stats_acc_perf"))

	# Data_df = data_df[:1000]
	# Randomize data
	data_df = data_df.reindex(np.random.permutation(data_df.index))

	# Replace NaN with 0(zero) or -999. so it doesnt skew the data.
	data_df = data_df.replace("NaN",0).replace("N/A",0)

	X = np.array(data_df[FEATURES].values)

	y = (data_df["Status"]
		 .replace("underperform",0)
		 .replace("outperform",1)
		 .values.tolist())

	X = preprocessing.scale(X)

	# Were gonna check for precentage change
	Z = np.array(data_df[["stock_p_change","sp500_p_change"]])

	return X,y,Z


def Analysis(withNA,enhanced):

	test_size = 1000

	invest_amount = 10000
	total_invests = 0
	if_market = 0 # If you invested in the Market
	if_strat = 0 # If you invested in the Strategy

	X, y , Z = Build_Data_Set(withNA,enhanced)
	print(len(X))

	# Using SVC
	clf = svm.SVC(kernel="linear", C= 1.0)
	clf.fit(X[:-test_size],y[:-test_size])

	correct_count = 0

	# Now run the Test Data.
	for x in range(1, test_size+1):
		# If our prediction was correct
		if clf.predict(X[-x])[0] == y[-x]:
			correct_count += 1

		# If we predicted 1(to invest)
		if clf.predict(X[-x])[0] == 1:
			invest_return = invest_amount + (invest_amount * (Z[-x][0]/100))
			market_return = invest_amount + (invest_amount * (Z[-x][1]/100))
			total_invests += 1
			if_market += market_return
			if_strat += invest_return




	data_df = pd.DataFrame.from_csv("./data/"+fileToSave(withNA,enhanced,"yahooReq_sample"))

	# Replace NaN with 0(zero) or -999. so it doesnt skew the data.
	data_df = data_df.replace("NaN",0).replace("N/A",0)

	X = np.array(data_df[FEATURES].values)

	X = preprocessing.scale(X)

	Z = data_df["Ticker"].values.tolist()

	invest_list = []

	# Each row in yahoo_sample
	for i in range(len(X)):

		# Make prediction
		p = clf.predict(X[i])[0]

		# If we predicted to invest
		if p==1:
			# print(Z[i])
			invest_list.append(Z[i])

	print("invest_List:",invest_list)
	print("invest_List size:",len(invest_list))

# Analysis(include NA?, want enhanced?)
Analysis(False,False)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk
from sklearn import neighbors
#%%
def missingValue(data):
	for col in data:
		if str(data[col].dtype) !='object' and str(data[col].dtype) !='int64':
			if len(data[data[col].isnull()]) > 0:
				train = data[data[col].notnull()]
				test = data[data[col].isnull()]
				data[col]=impute(train,test,col)
		if str(data[col].dtype) =='object':
			data[col] = data[col].astype("category")
	return data
def catmiss(data):
	trn = data[data['Outlet_Size'].notnull()]
	tst = data[data['Outlet_Size'].isnull()]
	trnx = trn.drop('Outlet_Size',axis=1)
	trny = trn['Outlet_Size']
	tstx = tst.drop('Outlet_Size',axis=1)
	knn = neighbors.KNeighborsClassifier()
	
def impute(train,test,col):
	if col=='Outlet_Establishment_Year':
		test[col] = train[col].median()
	else:
		test[col]=train[col].mean()
	return pd.Series(np.concatenate([train[col],test[col]]))
			
#%%

data = pd.read_csv("https://datahack-prod.s3.ap-south-1.amazonaws.com/train_file/Train_UWu5bXk.csv")
data = pd.DataFrame(data)
print(data.describe())
data = data.ix[:,1:] # removing index column
dat  = missingValue(data)
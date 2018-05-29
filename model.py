import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

def Read_dataset():
	return pd.read_csv("sdpair.csv")

def Get_Dict(csv):

	Disease_Type = []
	index = []
	
	i = 1
	for x in csv.disease:
		m = x.split(' ')
		for Type in m:
			if Type not in Disease_Type:
				Disease_Type.append(Type)
				index.append(i)
				i = i + 1

	del Disease_Type[0]
	keys = Disease_Type
	values = index

	return dict(zip(values, keys))
	

if __name__ == "__main__":

	csv = Read_dataset()

	Dict = Get_Dict(csv)

	print(Dict, end = '\n')

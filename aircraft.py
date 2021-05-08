import pandas as pd
import pickle
import numpy as np
train=pd.read_csv('train.csv')
x=train[['Safety_Score','Days_Since_Inspection','Control_Metric','Adverse_Weather_Metric']]
y=train['Severity']
from sklearn.ensemble import BaggingClassifier
bagging = BaggingClassifier(base_estimator= None,max_features= 1.0, max_samples= 0.98, n_estimators= 200)
bagging.fit(x,y)
pickle.dump(bagging,open('model.pkl','wb'))
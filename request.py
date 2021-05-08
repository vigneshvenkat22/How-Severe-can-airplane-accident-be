import requests


url = 'http://localhost:5000/predict_api'

r = requests.post(url,json={'Days_Since_Inspection':2, 'Adverse_Weather_Metric':1, 'Control_Metric':0.784545,'Safety_Score':35})



print(r.json())


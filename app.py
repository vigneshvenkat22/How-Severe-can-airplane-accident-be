from flask import Flask ,render_template, request
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import BaggingClassifier


app = Flask(__name__)


model= pickle.load(open('model.pkl','rb'))

# Home Route
@app.route('/')
def home():
	return render_template('index.html')

# prediction

@app.route('/predict',methods=['POST'])
def predict():
	int_feature = [float(x) for x in request.form.values()]
	final_features = [np.array(int_feature)]
	prediction = model.predict(final_features[:])
	output = prediction[0]
	x = "The Severity of the accident could be "
	if output== 0:
		y = 'Highly Fatal and Damaging'
	elif output==1:
		y = 'Significant Damage and Serious Injuries'	
	elif output == 2:
			y = 'Minor Damage and Injuries'
	elif output ==3:
			y = 'Significant Damage and Fatalities'
	return render_template('index.html',text = x ,predictiontext= y)


if __name__ == "__main__":
	app.run(debug=True)

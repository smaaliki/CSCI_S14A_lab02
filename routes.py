# Following site was used as reference on how to deploy the pkl file with Flask  
#https://blog.hyperiondev.com/index.php/2018/02/01/deploy-machine-learning-model-flask-api/

from flask import Flask, render_template
from sklearn.externals import joblib

app = Flask(__name__)

@app.route("/")

def index():
	prediction_input=[[4, 2.5, 3005, 15,17903.0,0,0,1]]
	#prediction_input.reshape(1,-1)
	prediction = model.predict(prediction_input).round(2)
	return render_template("index.html", prediction="${:,.2f}".format(prediction[0]))

if __name__ == "__main__":
	model = joblib.load('dregr.pkl')
	app.run(debug=True)
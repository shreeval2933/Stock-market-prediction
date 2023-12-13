from flask import Flask, render_template, url_for, request
import pandas as pd
import pickle

app=Flask(__name__)

with open('final_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input values from the HTML form
        input1 = float(request.form['message1'])
        input2 = float(request.form['message2'])
        input3 = float(request.form['message3'])
        input4 = float(request.form['message4'])

        # Make a prediction using the loaded model
        prediction = model.predict([[input1, input2, input3, input4]])
        result = 'Up' if prediction[0] == 1 else 'Down'

        return render_template('index.html',prediction='Tommorow Nifty will go {}'.format(result))
    
if __name__== '__main__':
    app.run(debug=True)
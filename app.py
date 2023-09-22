from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
model=pickle.load(open('model/best_model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        # Get user input from the form
        company = request.form['company']
        typename = request.form['typename']
        inches = float(request.form['inches'])
        ram = int(request.form['ram'])
        weight = float(request.form['weight'])
        ssd = int(request.form['ssd'])
        hdd = int(request.form['hdd'])
        touchscreen = int(request.form['touchscreen'])
        ips = int(request.form['ips'])
        cpu_brand = request.form['cpu_brand']
        gpu_brand = request.form['gpu_brand']
        os = request.form['os']

        # Create a DataFrame with the user input
        user_input = pd.DataFrame({
            'Company': [company],
            'TypeName': [typename],
            'Inches': [inches],
            'Ram': [ram],
            'Weight': [weight],
            'SSD': [ssd],
            'HDD': [hdd],
            'Touchscreen': [touchscreen],
            'IPS': [ips],
            'Cpu_Brand': [cpu_brand],
            'Gpu_Brand': [gpu_brand],
            'OS': [os]
        })

        # Make predictions using the model
        prediction = model.predict(user_input)

        return f'Predicted Price: ${prediction[0]:,.2f}'

if __name__ == '__main__':
    app.run(host="0.0.0.0")


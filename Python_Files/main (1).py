import pandas as pd
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the pre-trained Linear Regression model from a pickled file
with open('LinearRRegressionModel.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extract input values from the form
        car_model = request.form["model"]
        year = int(request.form['year'])
        transmission = request.form['transmission']
        total_driven = float(request.form['total_driven'])
        fuelType = request.form['fuelType']
        tax = float(request.form['tax(£)'])
        mpg = float(request.form['mpg'])
        engineSize = float(request.form['engineSize'])

        # Create a DataFrame with the input data
        input_data = pd.DataFrame({
            'model': [car_model],
            'year': [year],
            'transmission': [transmission],
            'total_driven': [total_driven],
            'fuelType': [fuelType],
            'tax(£)': [tax],
            'mpg': [mpg],
            'engineSize': [engineSize]
        })

        # Print input data for verification
        print("Input Data:")
        print(input_data)

        # Make a prediction using the loaded model
        prediction = model.predict(input_data)

        # Print the prediction for display
        print("Prediction:")
        print(prediction)

        # Return the prediction to the webpage
        return render_template('index.html', prediction=f"Predicted Price: £{prediction[0]:.2f}")

    # When the page loads initially
    return render_template('index.html', prediction="")

if __name__ == "__main__":
    app.run(debug=True)

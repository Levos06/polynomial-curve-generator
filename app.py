from flask import Flask, render_template, request
import numpy as np
from numpy.polynomial import Polynomial

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def result():
    x_values = []
    y_values = []

    for key in request.form:
        if key.startswith('x_'):
            x_values.append(float(request.form[key]))
        elif key.startswith('y_'):
            y_values.append(float(request.form[key]))

    if len(x_values) == 0 or len(x_values) != len(y_values):
        return "Invalid input data. Please provide valid x and y values."

    degree = min(3, len(x_values) - 1)
    coefficients = np.polyfit(x_values, y_values, degree)
    polynomial = Polynomial(coefficients)

    terms = [f"{round(coef, 5)}x^{deg}" for deg, coef in enumerate(coefficients[::-1]) if abs(coef) >= 0.0001]
    polynomial_formula = " + ".join(terms[::-1])

    return render_template('index.html', result=polynomial_formula)

if __name__ == '__main__':
    app.run(debug=True)

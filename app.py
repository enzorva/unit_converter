from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    value = float(request.form['value'])
    category = request.form['category']
    result = 0

    if category == 'length':
        from_unit = request.form['from-length']
        to_unit = request.form['to-length']
        result = convert_length(value, from_unit, to_unit)
    elif category == 'weight':
        from_unit = request.form['from-weight']
        to_unit = request.form['to-weight']
        result = convert_weight(value, from_unit, to_unit)
    elif category == 'temperature':
        from_unit = request.form['from-temperature']
        to_unit = request.form['to-temperature']
        result = convert_temperature(value, from_unit, to_unit)

    return render_template('index.html', result=result)

@app.route('/length')
def length():
    return render_template('length.html')

def convert_length(value, from_unit, to_unit):
    conversions= {
        'meters': 1,
        'kilometers': 0.001,
        'centimeters': 100,
        'millimeters': 1000,
        'inches': 39.3701,
        'feet': 3.28084,
        'yards': 1.09361,
        'miles': 0.000621371
    }

    return value * conversions[to_unit] / conversions[from_unit]

def convert_weight(value, from_unit, to_unit):
    conversions = {
        'grams': 1,
        'kilograms': 0.001,
        'milligrams': 1000,
        'pounds': 0.00220462,
        'ounces': 0.035274
    }

    return value * conversions[to_unit] / conversions[from_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
    return value  

if __name__ == '__main__':
    app.run(debug=True)
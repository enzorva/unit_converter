from flask import Flask, request, render_template

app = Flask(__name__)



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

@app.route('/')
def default():
    return render_template('length.html')

@app.route('/length')
def length():
    return render_template('length.html')

@app.route('/weight')
def weight():
    return render_template('weight.html')

@app.route('/temperature')
def temperature():
    return render_template('temperature.html')

@app.route('/convert_length', methods=['POST'])
def convert_length_route():
    value = request.form['value']
    from_unit = request.form['from_unit']
    to_unit = request.form['to_unit']
    result, from_abbr, to_abbr = convert_length(value, from_unit, to_unit)
    print_result = f"{value} {from_abbr} = {result} {to_abbr}"
    return render_template('length_result.html', result=print_result)

@app.route('/convert_weight', methods=['POST'])
def convert_weight_route():
    value = request.form['value']
    from_unit = request.form['from_unit']
    to_unit = request.form['to_unit']
    result, from_abbr, to_abbr = convert_weight(value, from_unit, to_unit)
    print_result = f"{value} {from_abbr} = {result} {to_abbr}"
    return render_template('weight_result.html', result=print_result)

@app.route('/convert_temperature', methods=['POST'])
def convert_temperature_route():
    value = request.form['value']
    from_unit = request.form['from_unit']
    to_unit = request.form['to_unit']
    result, from_abbr, to_abbr = convert_temperature(value, from_unit, to_unit)
    print_result = f"{value} {from_abbr} = {result} {to_abbr}"
    return render_template('temperature_result.html', result=print_result)

def convert_length(value, from_unit, to_unit):
    value = float(value)
    conversions = {
        'meters': ('m', 1),
        'kilometers': ('km', 0.001),
        'centimeters': ('cm', 100),
        'millimeters': ('mm', 1000),
        'inches': ('in', 39.3701),
        'feet': ('ft', 3.28084),
        'yards': ('yd', 1.09361),
        'miles': ('mi', 0.000621371)
    }

    from_abbr, from_factor = conversions[from_unit]
    to_abbr, to_factor = conversions[to_unit]
    result = round(value * to_factor / from_factor,2)
    return result, from_abbr, to_abbr

def convert_weight(value, from_unit, to_unit):
    value = float(value)
    conversions = {
        'grams': ('g', 1),
        'kilograms': ('kg', 0.001),
        'milligrams': ('mg', 1000),
        'pounds': ('lbs', 0.00220462),
        'ounces': ('oz', 0.035274)
    }
    from_abbr, from_factor = conversions[from_unit]
    to_abbr, to_factor = conversions[to_unit]
    result = round(value * to_factor / from_factor,2)
    return result, from_abbr, to_abbr

def convert_temperature(value, from_unit, to_unit):
    value = float(value)
    abbreviations = {
        'Celsius': 'C',
        'Fahrenheit': 'F',
        'Kelvin': 'K'
    }

    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            result = (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            result = value + 273.15
        else:
            result = value
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            result = (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            result = (value - 32) * 5/9 + 273.15
        else:
            result = value
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            result = value - 273.15
        elif to_unit == 'Fahrenheit':
            result = (value - 273.15) * 9/5 + 32
        else:
            result = value
    else:
        result = value

    return result, abbreviations[from_unit], abbreviations[to_unit]

if __name__ == '__main__':
    app.run(debug=True)
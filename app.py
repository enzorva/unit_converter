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

def normalize_unit(unit, category):
    unit_mappings = {
        'length': {
            'm': 'meters', 'meters': 'meters',
            'km': 'kilometers', 'kilometers': 'kilometers',
            'cm': 'centimeters', 'centimeters': 'centimeters',
            'mm': 'millimeters', 'millimeters': 'millimeters',
            'in': 'inches', 'inches': 'inches',
            'ft': 'feet', 'feet': 'feet',
            'yd': 'yards', 'yards': 'yards',
            'mi': 'miles', 'miles': 'miles'
        },
        'weight': {
            'g': 'grams', 'grams': 'grams',
            'kg': 'kilograms', 'kilograms': 'kilograms',
            'mg': 'milligrams', 'milligrams': 'milligrams',
            'lbs': 'pounds', 'pounds': 'pounds',
            'oz': 'ounces', 'ounces': 'ounces'
        },
        'temperature': {
            'c': 'Celsius', 'celsius': 'Celsius',
            'f': 'Fahrenheit', 'fahrenheit': 'Fahrenheit',
            'k': 'Kelvin', 'kelvin': 'Kelvin'
        }
    }

    normalized = unit.lower()
    for abbr, full_name in unit_mappings[category].items():
        if normalized == abbr or normalized == full_name.lower():
            return full_name
    return None

def normalize_value(value):
    return float(value.replace(',', '.')) if ',' in value else float(value)

def format_result(value, from_abbr, result, to_abbr):
    if abs(result - round(result, 3)) > 0:
        return f"{value} {from_abbr} ≈ {round(result, 3)} {to_abbr}"
    else:
        return f"{value} {from_abbr} = {result} {to_abbr}"

@app.route('/convert_length', methods=['POST'])
def convert_length_route():
    value = normalize_value(request.form['value'])
    from_unit = normalize_unit(request.form['from_unit'], 'length')
    to_unit = normalize_unit(request.form['to_unit'], 'length')
    result, from_abbr, to_abbr = convert_length(value, from_unit, to_unit)
    print_result = format_result(value, from_abbr, result, to_abbr)
    return render_template('length_result.html', result=print_result)

@app.route('/convert_weight', methods=['POST'])
def convert_weight_route():
    value = normalize_value(request.form['value'])
    from_unit = normalize_unit(request.form['from_unit'], 'weight')
    to_unit = normalize_unit(request.form['to_unit'], 'weight')
    result, from_abbr, to_abbr = convert_weight(value, from_unit, to_unit)
    print_result = format_result(value, from_abbr, result, to_abbr)
    return render_template('weight_result.html', result=print_result)

@app.route('/convert_temperature', methods=['POST'])
def convert_temperature_route():
    value = normalize_value(request.form['value'])
    from_unit = normalize_unit(request.form['from_unit'], 'temperature')
    to_unit = normalize_unit(request.form['to_unit'], 'temperature')
    result, from_abbr, to_abbr = convert_temperature(value, from_unit, to_unit)
    print_result = format_result(value, from_abbr, result, to_abbr)
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
    result = value * to_factor / from_factor
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
    result = value * to_factor / from_factor
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
            result = round((value * 9/5) + 32, 2)
        elif to_unit == 'Kelvin':
            result = round(value + 273.15, 2)
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
            result = (value - 273.15) * 9/5 + 32, 2
        else:
            result = value
    else:
        result = value

    return result, abbreviations[from_unit], abbreviations[to_unit]

if __name__ == '__main__':
    app.run(debug=True)
# Unit Converter

This is a Flask-based web application for converting units of measurement. It supports conversions for:
- Length
- Weight
- Temperature

## Features
- User-friendly interface for selecting and converting units.
- Validation for input values and units.
- Displays supported units for each category.
- Handles user input variations (e.g., abbreviations, case sensitivity, and commas in numeric values).

## Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd unit_converter
   ```
3. Install the required dependencies:
   ```bash
   pip install flask
   ```

## Usage
1. Run the application:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Deployment
To share this application with others, you can deploy it using platforms like Heroku, Render, or Railway. Alternatively, you can use a tunneling service like ngrok to expose your local server to the internet.

## Inspiration
This project was inspired by the following webpage:
[Unit Converter Inspiration](https://roadmap.sh/projects/unit-converter)
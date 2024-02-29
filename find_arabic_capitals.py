import webbrowser
from flask import Flask, render_template, request

app = Flask(__name__)

# Dictionary mapping Arab countries to their capitals
arab_countries_capitals = {
    'Algeria': 'Algiers',
    'Bahrain': 'Manama',
    'Comoros': 'Moroni',
    'Djibouti': 'Djibouti',
    'Egypt': 'Cairo',
    'Iraq': 'Baghdad',
    'Jordan': 'Amman',
    'Kuwait': 'Kuwait City',
    'Lebanon': 'Beirut',
    'Libya': 'Tripoli',
    'Mauritania': 'Nouakchott',
    'Morocco': 'Rabat',
    'Oman': 'Muscat',
    'Palestine': 'Jerusalem',
    'Qatar': 'Doha',
    'Saudi Arabia': 'Riyadh',
    'Somalia': 'Mogadishu',
    'Sudan': 'Khartoum',
    'Syria': 'Damascus',
    'Tunisia': 'Tunis',
    'United Arab Emirates': 'Abu Dhabi',
    'Yemen': 'Sanaa'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_capital', methods=['POST'])
def get_capital():
    country = request.form['country']
    capital = arab_countries_capitals.get(country)
    if capital:
        return capital
    else:
        return 'Country not found!'

if __name__ == '__main__':
    # Open web browser automatically
    webbrowser.open('http://127.0.0.1:5000/')
    # Start Flask server
    app.run(debug=True)

from flask import Flask, render_template
import requests


app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def index():
    api_url = 'https://pokeapi.co/api/v2/pokemon?limit=100&offset=0'  # URL corregida

    response = requests.get(api_url)

    data = response.json()
    pokes = data['results']
    return render_template('index.html', pokes=pokes)




if __name__ == '__main__':
    app.run()

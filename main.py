
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap

from functions import *


app = Flask(__name__)

app.config['SECRET_KEY'] = 'somestringfornow123a1!@asf2@!#$'

Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/characters")
def character_list():
    characters_json = get_data_from_api(query="characters")
    return render_template('characters.html', characters=characters_json['data']['results'])


if __name__ == '__main__':
    app.run(debug=True)


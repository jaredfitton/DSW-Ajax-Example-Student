from flask import Flask, redirect, url_for, session, request, jsonify, Markup
from flask import render_template

app = Flask(__name__)

app.debug = True #Change this to False for production

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/update_div1', methods=['POST'])
def update():
    print((request.form)['clientMessage'])
    return Markup('<p>This text was sent from the server</p>')

if __name__ == '__main__':
    app.run()

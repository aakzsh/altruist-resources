from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/resources')
def sources():
    return render_template('resources.html')







# Driver Code


if __name__ == '__main__':
    # function call
    app.run(debug=True)

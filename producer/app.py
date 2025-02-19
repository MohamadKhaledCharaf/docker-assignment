from flask import Flask
import random

app = Flask(__name__)

@app.route('/data')
def data():
    # Return a random number as a string
    return str(random.randint(1, 100))

if __name__ == '__main__':
    # Listen on all interfaces at port 5000
    app.run(host='0.0.0.0', port=5000)

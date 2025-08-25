from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello Home'

@app.route('/about')
def about():
    return '<h1>Hello About</h1>'

if __name__ == '__main__':
    app.run(debug=True)

#How to Run:

Save the code in a file, e.g., app.py

Run it:
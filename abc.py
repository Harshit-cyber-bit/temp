from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '21BCS8539'

if __name__ == '__main__':
    app.run(debug=True)

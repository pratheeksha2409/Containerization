from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def hello():
    print("Application is running!", file=sys.stdout)
    return 'This is a flask application running in Container 2'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


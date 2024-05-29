from flask import Flask
from routes import analyse_route

app = Flask(__name__)

analyse_route.register_route(app)

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5000)
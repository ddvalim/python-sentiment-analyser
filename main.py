from flask import Flask
from routes import analyse_route
from service import analyser_service
from controller import analyser_controller

app = Flask(__name__)

analyser_service = analyser_service.Analyser_Service()
analyser_controller = analyser_controller.Analyser_Controller(analyser_service=analyser_service)

analyse_route.register_route(app, analyser_controller=analyser_controller)

if __name__ == '__main__':
    app.run()


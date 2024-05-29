from flask import Flask, request, jsonify
from controller import analyser_controller

def register_route(app):

    @app.route('/analyse',methods=['POST'])
    def analyse():
        body = request.get_json('text')

        ctrl = analyser_controller.Analyser_Controller()

        predicted_class, confidence, probabilities = ctrl.analyse(body['text'])

        print(predicted_class)
        print(confidence)
        print(probabilities)
        
        return jsonify(
            predicted_class=predicted_class
        )
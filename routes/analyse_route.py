from flask import Flask, request, jsonify
from controller import analyser_controller

def register_route(app):

    @app.route('/',methods=['GET'])
    def analyse():
        text = request.form.get('text')

        ctrl = analyser_controller.Analyser_Controller()

        predicted_class, confidence, probabilities = ctrl.analyse(text)

        print(predicted_class)
        print(confidence)
        print(probabilities)
        
        return jsonify(
            predicted_class=predicted_class,
            confidence=confidence
        )
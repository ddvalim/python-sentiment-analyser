from flask import Flask, request, jsonify

def register_route(app, analyser_controller):

    @app.route('/',methods=['GET'])
    def analyse():
        text = request.form.get('text')

        predicted_class, confidence, probabilities = analyser_controller.analyse(text)

        print(predicted_class)
        print(confidence)
        print(probabilities)
        
        return jsonify(
            predicted_class=predicted_class,
            confidence=confidence
        )
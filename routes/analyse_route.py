from flask import Flask, request, jsonify

def register_route(app, analyser_controller):

    @app.route('/',methods=['GET'])
    def analyse():
        text = request.form.get('text')

        res = analyser_controller.analyse(text)
        
        return 'analyser'
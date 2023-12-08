## app.py
from flask import Flask, request, jsonify
from data_generator import DataGenerator
from forecaster import Forecaster

class App:
    def __init__(self):
        self.app = Flask(__name__)
        self.data_generator = DataGenerator()
        self.forecaster = Forecaster()

        @self.app.route('/forecast', methods=['POST'])
        def forecast():
            try:
                years = int(request.json.get('years', 1))
            except (TypeError, ValueError):
                return jsonify(error="Invalid 'years' parameter"), 400

            self.data_generator.years = years
            data = self.data_generator.generate()
            forecast = self.forecaster.forecast(data)
            return jsonify(forecast=forecast['yhat'].tolist())

    def run(self):
        self.app.run(debug=True)

from flask import Flask, jsonify
from flask_cors import CORS
import csv
import random

app = Flask(__name__)
CORS(app)

def load_coffee_facts():
    with open('coffeefact.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        return [row[0] for row in reader]
    
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Coffee Fact API! Use /coffee-fact to get a random fact."
    
@app.route('/coffee-fact', methods=['GET'])
def get_coffee_fact():
    facts = load_coffee_facts()
    return jsonify({"fact": random.choice(facts)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
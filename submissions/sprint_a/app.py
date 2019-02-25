from sprint_a import app
from flask import jsonify

@app.route('/')
def generate_epithets():
    epithet = jsonify({'epithets': []})
    return epithet


@app.route('/vocabulary')
def vocabulary():
    vocab = jsonify({'vocabulary': {}})
    return vocab
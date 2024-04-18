from flask import Flask, Flast, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')


# This will act as our temporary database
todos = [
    {"label": "Sample Todo 1", "done": True},
    {"label": "Sample Todo 2", "done": True}
]

@app.route('/')
def index():
    return "Welcome to the Flask To-Do API!"

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    if not request.json or 'label' not in request.json or 'done' not in request.json:
        # Bad request if the JSON is invalid or missing keys
        return jsonify({'error': 'Invalid todo format'}), 400

    new_todo = {
        'label': request.json['label'],
        'done': request.json['done']
    }
    todos.append(new_todo)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < 0 or position >= len(todos):
        # Not found if the position is out of range
        return jsonify({'error': 'Todo not found'}), 404

    todos.pop(position)
    return jsonify(todos)

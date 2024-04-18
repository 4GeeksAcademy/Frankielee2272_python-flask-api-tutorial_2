from flask import Flask, jsonify, request

app = Flask(__name__)

# Define the global 'todos' list to manage todo items.
todos = [
    {"label": "My first task", "done": False}
]

@app.route('/todos', methods=['GET'])
def get_todos():
    # Return the entire list of todos as a JSON response.
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    # Add a new todo item from the request JSON body to the todos list.
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos), 201

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    # Check if the position is within the bounds of the todos list.
    if 0 <= position < len(todos):
        # If valid, remove the todo item at the specified position.
        todos.pop(position)
        # Return the updated list of todos with a 200 OK status.
        return jsonify(todos), 200
    else:
        # If the position is out of range, return an error message with a 404 Not Found status.
        return jsonify({"error": "Todo not found at position " + str(position)}), 404

@app.route('/myroute', methods=['GET'])
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Start the Flask application with the specified host and port.
    app.run(host='0.0.0.0', port=3245, debug=True)

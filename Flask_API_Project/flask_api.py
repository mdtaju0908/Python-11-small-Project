"""
Flask API Project - A simple RESTful API using Flask
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data storage
tasks = [
    {"id": 1, "title": "Learn Python", "completed": False},
    {"id": 2, "title": "Build API", "completed": False},
    {"id": 3, "title": "Deploy App", "completed": False}
]


def get_next_id():
    """Get the next available task ID."""
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


@app.route("/", methods=["GET"])
def home():
    """Home route."""
    return jsonify({
        "message": "Welcome to Flask API Project",
        "endpoints": {
            "GET /tasks": "Get all tasks",
            "GET /tasks/<id>": "Get task by ID",
            "POST /tasks": "Create a new task",
            "PUT /tasks/<id>": "Update a task",
            "DELETE /tasks/<id>": "Delete a task"
        }
    })


@app.route("/tasks", methods=["GET"])
def get_tasks():
    """Get all tasks."""
    return jsonify({"tasks": tasks, "count": len(tasks)})


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    """Get a specific task by ID."""
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task)


@app.route("/tasks", methods=["POST"])
def create_task():
    """Create a new task."""
    if not request.json or "title" not in request.json:
        return jsonify({"error": "Title is required"}), 400

    new_task = {
        "id": get_next_id(),
        "title": request.json["title"],
        "completed": request.json.get("completed", False)
    }
    tasks.append(new_task)
    return jsonify(new_task), 201


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    """Update an existing task."""
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404

    if not request.json:
        return jsonify({"error": "No data provided"}), 400

    task["title"] = request.json.get("title", task["title"])
    task["completed"] = request.json.get("completed", task["completed"])
    return jsonify(task)


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """Delete a task."""
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404

    tasks.remove(task)
    return jsonify({"message": "Task deleted successfully"})


@app.route("/tasks/completed", methods=["GET"])
def get_completed_tasks():
    """Get all completed tasks."""
    completed = [t for t in tasks if t["completed"]]
    return jsonify({"tasks": completed, "count": len(completed)})


@app.route("/tasks/pending", methods=["GET"])
def get_pending_tasks():
    """Get all pending tasks."""
    pending = [t for t in tasks if not t["completed"]]
    return jsonify({"tasks": pending, "count": len(pending)})


@app.errorhandler(404)
def not_found(_error):
    """Handle 404 errors."""
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def internal_error(_error):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    print("=" * 50)
    print("       Flask API Project")
    print("=" * 50)
    print("\nAvailable endpoints:")
    print("  GET  /           - Home (API info)")
    print("  GET  /tasks      - Get all tasks")
    print("  GET  /tasks/<id> - Get task by ID")
    print("  POST /tasks      - Create task")
    print("  PUT  /tasks/<id> - Update task")
    print("  DELETE /tasks/<id> - Delete task")
    print("  GET  /tasks/completed - Get completed tasks")
    print("  GET  /tasks/pending   - Get pending tasks")
    print("\n" + "=" * 50)

    app.run(debug=True, host="0.0.0.0", port=5000)

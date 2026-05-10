import os
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Todo
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
if app.config['SQLALCHEMY_DATABASE_URI'] and app.config['SQLALCHEMY_DATABASE_URI'].startswith("postgres://"):
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI'].replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-secret-key')

# Initialize DB and Migrate
db.init_app(app)
migrate = Migrate(app, db)

# --- Endpoints ---

@app.route('/')
def index():
    return jsonify({
        "message": "Welcome to the To-Do List API",
        "endpoints": {
            "GET /health": "Health check status",
            "GET /todos": "List all to-dos",
            "POST /todos": "Create a new to-do",
            "GET /todos/<id>": "Get one to-do",
            "PUT /todos/<id>": "Update a to-do",
            "DELETE /todos/<id>": "Delete a to-do"
        }
    })

@app.route('/health')
def health_check():
    try:
        # Test database connection
        db.session.execute(db.text('SELECT 1'))
        return jsonify({
            "status": "healthy",
            "database": "connected"
        }), 200
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "database": str(e)
        }), 500

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([todo.to_dict() for todo in todos]), 200

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    
    if not data or not data.get('title'):
        return jsonify({"error": "Title is required"}), 400
    
    new_todo = Todo(
        title=data.get('title'),
        description=data.get('description', '')
    )
    
    db.session.add(new_todo)
    db.session.commit()
    
    return jsonify(new_todo.to_dict()), 201

@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    return jsonify(todo.to_dict()), 200

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No data provided"}), 400
        
    todo.title = data.get('title', todo.title)
    todo.description = data.get('description', todo.description)
    todo.done = data.get('done', todo.done)
    
    db.session.commit()
    
    return jsonify(todo.to_dict()), 200

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"message": "Todo deleted successfully"}), 200

# Error Handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

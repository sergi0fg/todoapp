from flask import Flask
from routes.routes import todo_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(todo_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

def create_app():
    app = Flask(__name__)
    app.register_blueprint(todo_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

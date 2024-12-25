from flask import Flask, render_template
from routes.project_routes import project_blueprint
from routes.column_routes import column_blueprint
from routes.task_routes import task_blueprint
from routes.log_routes import log_blueprint
from routes.user_routes import user_blueprint
from database import Base, engine
import os

Base.metadata.create_all(engine)

app = Flask(__name__, template_folder='templates')

# Регистрация blueprint
app.register_blueprint(project_blueprint)
app.register_blueprint(column_blueprint)
app.register_blueprint(task_blueprint)
app.register_blueprint(log_blueprint)
app.register_blueprint(user_blueprint)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
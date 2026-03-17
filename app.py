from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

# Create SQLite database instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

# Define model of a to-do list task

class Task(db.Model):
    # db.Column reps a col in the database
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now())
@app.route('/', methods=['GET','POST'])
def index():
    # add new task into database
    if request.method =='POST':
        task_content = request.form.get('content')
        new_task = Task(content=task_content)
        # Put new Task in Database
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'Error adding task!'
    all_tasks = Task.query.all()
    return render_template('index.html', tasks=all_tasks)

@app.route('/delete/<int:task_id>')
def delete(task_id):
    task=Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect('/')
    











# Create Database in Main method

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)

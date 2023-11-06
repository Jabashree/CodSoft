from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    new_task = request.form.get('task')
    if new_task.strip():
        tasks.append(new_task)
    return redirect(url_for('index'))

@app.route('/edit_task/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    updated_task = request.form.get('updated_task')
    if updated_task.strip():
        tasks[task_id] = updated_task
    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
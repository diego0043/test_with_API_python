from flask import Flask, render_template, request
import requests


app = Flask(__name__)
app.static_folder = 'static'


def get_tasks(api_url):
    response = requests.get(api_url)
    tasks = response.json()
    return tasks


def add_task(api_url):
    titulo = request.form['titulo']
    descripcion = request.form['descripcion']
    task = {'titulo': titulo, 'descripcion': descripcion, 'completada': "false"}
    response = requests.post(api_url, json=task)
    return response


def update_task(api_url, task_id, task):
    response = requests.put(api_url + task_id, data=task)
    return response


def delete_task(api_url, task_id):
    response = requests.delete(api_url + task_id)
    return response


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def index():

    api_url = 'https://todo-backend-u3wj.onrender.com/todo/'

    if request.method == "GET":
        tasks = get_tasks(api_url)
        return render_template('index.html', tasks=tasks)
    elif request.method == "POST":
        if request.form.get('_method') == 'DELETE':
            id = request.form['task_id']
            delete_task(api_url, id)
            tasks = get_tasks(api_url)
            return render_template('index.html', tasks=tasks)
        else:
            add_task(api_url)
            tasks = get_tasks(api_url)
            return render_template('index.html', tasks=tasks)

    elif request.method == "PUT":
        task_id = request.form['task_id']
        task = request.form['task']
        response = requests.put(api_url + task_id, data={'title': task})
        return response.text
    elif request.method == "DELETE":
        task_id = request.form['task_id']
        response = requests.delete(api_url + task_id)
        return response.text


if __name__ == '__main__':
    app.run()

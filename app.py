from flask import Flask, render_template

app = Flask(__name__)
app.static_folder = 'static'

tareas = [
    {'id': 1, 'nombre': 'Tarea 1', 'descripcion': 'Descripción de la tarea 1'},
    {'id': 2, 'nombre': 'Tarea 2', 'descripcion': 'Descripción de la tarea 2'},
    {'id': 3, 'nombre': 'Tarea 3', 'descripcion': 'Descripción de la tarea 3'},
    {'id': 4, 'nombre': 'Tarea 4', 'descripcion': 'Descripción de la tarea 4'},
    {'id': 5, 'nombre': 'Tarea 5', 'descripcion': 'Descripción de la tarea 5'},
    {'id': 6, 'nombre': 'Tarea 6', 'descripcion': 'Descripción de la tarea 6'},
    {'id': 7, 'nombre': 'Tarea 7', 'descripcion': 'Descripción de la tarea 7'},
    {'id': 8, 'nombre': 'Tarea 8', 'descripcion': 'Descripción de la tarea 8'},
    {'id': 9, 'nombre': 'Tarea 9', 'descripcion': 'Descripción de la tarea 9'}

]


@app.route('/')
def index():  # put application's code here
    return render_template('index.html', tareas=tareas)


if __name__ == '__main__':
    app.run()

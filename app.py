from flask import Flask, request
from flask.json import jsonify
from db import TasksDB

app = Flask(__name__)

db = TasksDB()

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'hello': 'world'})


@app.route('/tasks', methods=['GET', 'POST', 'PUT', 'DELETE'])
def tasks():
    if request.method == 'POST':
        body = request.get_json()
        collection_name = 'tasks'
        resp = db.insert_task(collection_name, body)
        if resp:
            return jsonify({'msg': 'tarea agregada correctamente'})
        else:
            return jsonify({'msg': 'hubo un problema al agregar la tarea'})

    if request.method == 'GET':
        resp = db.get_tasks('tasks')
        print(resp)
        return jsonify(resp)
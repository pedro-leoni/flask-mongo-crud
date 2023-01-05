from flask import Flask, request
from flask.json import jsonify
from db import TasksDB
import bson.json_util as json_util

import json

app = Flask(__name__)

db = TasksDB()

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'hello': 'world'})


@app.route('/tasks', methods=['GET', 'POST'])
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
        try:
            resp = db.get_tasks('tasks')
            return json_util.dumps(resp)
        except Exception as err:
            print(err)
            return jsonify({'msg': 'hubo un problema'})

@app.route('/tasks/<id>', methods=['PUT', 'DELETE'])
def tasks_with_param(id):
    if request.method == 'DELETE':
        try:
            db.delete_task('tasks', id)
            return jsonify({'msg': 'Tarea eliminada con exito'})
        except Exception as err:
            print(err)
            return jsonify({'msg': 'Hubo un problema al eliminar la tarea'})
        
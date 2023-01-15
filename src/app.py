from flask import Flask, request
from flask.json import jsonify
from db import TasksDB
import bson.json_util as json_util
# TODO validate

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
        try:
            db.insert_task(collection_name, body)
            return jsonify({'msg': 'Task created'})
        except Exception as err:
            return jsonify({'msg': f'{err}'})
        # if resp:
        #     return jsonify({'msg': 'tarea agregada correctamente'})
        # else:
        #     return jsonify({'msg': 'hubo un problema al agregar la tarea'})

    if request.method == 'GET':
        try:
            resp = db.get_tasks('tasks')
            return json_util.dumps(resp)
        except Exception as err:
            return jsonify({'msg': f'{err}'})


@app.route('/tasks/<id>', methods=['PUT', 'DELETE'])
def tasks_with_param(id):
    if request.method == 'DELETE':
        try:
            db.delete_task('tasks', id)
            return jsonify({'msg': 'Task deleted'})
        except Exception as err:
            return jsonify({'msg': f'{err}'})
    if request.method == 'PUT':
        body = request.get_json()
        try:
            db.edit_task('tasks', id, body)
            return jsonify({'msg': 'Task edited'})
        except Exception as err:
            return jsonify({'msg': f'{err}'})

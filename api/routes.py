# api/routes.py

from flask import Blueprint, jsonify, request, abort

api_bp = Blueprint('api', __name__)

tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Eggs, Fruits',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Find a good Python tutorial',
        'done': False
    }
]

disciplines = [
    {
        'id': 1,
        'name': 'Mathematical Analysis',
        'description': 'Study of numbers, shapes, and patterns',
        'grade': 5,
        'instructor': 'Masterov Ivan Viktorovich'
    },
    {
        'id': 2,
        'name': 'Linear Algebra',
        'description': 'Study of vectors and matrix',
        'grade': 4,
        'instructor': 'Boltovsky Dmitry Vladimirovich'
    }
]


@api_bp.route('/', methods=['GET'])
def get_routes():
    routes = {
        'routes': [
            {'path': '/api/tasks', 'description': 'Get all tasks'},
            {'path': '/api/tasks/<int:task_id>', 'description': 'Get a specific task'},
            {'path': '/api/disciplines', 'description': 'Get all disciplines'},
            {'path': '/api/disciplines/<int:discipline_id>', 'description': 'Get a specific discipline'},
        ]
    }
    return jsonify(routes)


@api_bp.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@api_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        abort(404)
    return jsonify({'task': task})


@api_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = {
        'id': tasks[-1]['id'] + 1 if tasks else 1,
        'title': data['title'],
        'description': data['description'],
        'done': False
    }
    tasks.append(new_task)
    return jsonify({'task': new_task}), 201


@api_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        abort(404)
    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    task['done'] = request.json.get('done', task['done'])
    return jsonify({'task': task})


@api_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        abort(404)
    tasks.remove(task)
    return jsonify({'result': True})


@api_bp.route('/disciplines', methods=['GET'])
def get_disciplines():
    return jsonify({'disciplines': disciplines})


@api_bp.route('/disciplines/<int:discipline_id>', methods=['GET'])
def get_discipline(discipline_id):
    discipline = next((d for d in disciplines if d['id'] == discipline_id), None)
    if discipline is None:
        abort(404)
    return jsonify({'discipline': discipline})


@api_bp.route('/disciplines', methods=['POST'])
def create_discipline():
    data = request.get_json()
    new_discipline = {
        'id': disciplines[-1]['id'] + 1 if disciplines else 1,
        'name': data['name'],
        'description': data['description'],
        'grade': data['grade'],
        'instructor': data['instructor']
    }
    disciplines.append(new_discipline)
    return jsonify({'discipline': new_discipline}), 201


@api_bp.route('/disciplines/<int:discipline_id>', methods=['PUT'])
def update_discipline(discipline_id):
    discipline = next((d for d in disciplines if d['id'] == discipline_id), None)
    if discipline is None:
        abort(404)
    discipline['name'] = request.json.get('name', discipline['name'])
    discipline['description'] = request.json.get('description', discipline['description'])
    discipline['grade'] = request.json.get('grade', discipline['grade'])
    discipline['instructor'] = request.json.get('instructor', discipline['instructor'])
    return jsonify({'discipline': discipline})


@api_bp.route('/disciplines/<int:discipline_id>', methods=['DELETE'])
def delete_discipline(discipline_id):
    discipline = next((d for d in disciplines if d['id'] == discipline_id), None)
    if discipline is None:
        abort(404)
    disciplines.remove(discipline)
    return jsonify({'result': True})

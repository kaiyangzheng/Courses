from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps


# init app
app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

db = SQLAlchemy(app)

# db models


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    admin = db.Column(db.Boolean)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)

# wrapper that makes a token required/gets the token from the header


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(
                token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.filter_by(
                public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

# get all users in user model


@app.route('/user', methods=['GET'])
@token_required
def get_all_users(current_user):

    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    users = User.query.all()
    output = []
    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['admin'] = user.admin
        output.append(user_data)
    return jsonify({'users': output})

# gets one user in the user model


@app.route('/user/<public_id>', methods=['GET'])
@token_required
def get_one_user(current_user, public_id):

    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({'message': 'No user found!'})
    user_data = {}
    user_data['public_id'] = user.public_id
    user_data['name'] = user.name
    user_data['password'] = user.password
    user_data['admin'] = user.admin
    return jsonify({'user': user_data})

# creates a user, must be admin to do so


@app.route('/user', methods=['POST'])
@token_required
def create_user(current_user):

    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(public_id=str(uuid.uuid4()),
                    name=data['name'], password=hashed_password, admin=False)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'New user created!'})


# promote user to admin


@app.route('/user/<public_id>', methods=['PUT'])
@token_required
def promote_user(current_user, public_id):

    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({'message': 'No user found!'})
    user.admin = True
    db.session.commit()
    return jsonify({'message': 'The user has been promoted!'})

# deletes user


@app.route('/user/<public_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, public_id):

    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({'message': 'No user found!'})
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'The user has been deleted!'})

# allows user to register


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data['name']
    password = data['password']
    if len(password) < 6:
        return jsonify({'error': "Password is too short"}), 400
    if len(name) < 3:
        return jsonify({'error': "Name is too short"}), 400
    if not name.isalnum() or " " in name:
        return jsonify({'error': "Name should be alphanumeric and include no spaces"}), 400
    if User.query.filter_by(name=name).first() is not None:
        return jsonify({'error': "Name is taken"}), 409
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(public_id=str(uuid.uuid4()), name=name,
                    password=hashed_password, admin=False)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'New user created!'})


# allows user to login and get token


@app.route('/login')
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
    user = User.query.filter_by(name=auth.username).first()
    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow(
        ) + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token': token})
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

# get all the todos of the current user


@app.route('/todo', methods=['GET'])
@token_required
def get_all_todos(current_user):
    todos = Todo.query.filter_by(user_id=current_user.id).all()
    output = []

    for todo in todos:
        todo_data = {}
        todo_data['id'] = todo.id
        todo_data['text'] = todo.text
        todo_data['complete'] = todo.complete
        output.append(todo_data)

    return jsonify({'todos': output})


# gets one todo of current user


@app.route('/todo/<todo_id>', methods=['GET'])
@token_required
def get_one_todo(current_user, todo_id):
    todo = Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()
    if not todo:
        return jsonify({'message': 'No todo found!'})
    todo_data = {}
    todo_data['id'] = todo.id
    todo_data['text'] = todo.text
    todo_data['complete'] = todo.complete
    return jsonify(todo_data)

# lets the current user create a todo


@app.route('/todo', methods=['POST'])
@token_required
def create_todo(current_user):
    data = request.get_json()
    new_todo = Todo(text=data['text'], complete=False, user_id=current_user.id)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({'message': 'Todo created!'})

# lets the current user upgrade todo to complete


@app.route('/todo/<todo_id>', methods=['PUT'])
@token_required
def complete_todo(current_user, todo_id):
    todo = Todo.query.filter_by(
        id=todo_id, user_id=current_user.id).first()
    if not todo:
        return jsonify({'message': 'No todo found!'})
    todo.complete = True
    db.session.commit()
    return jsonify({'message': 'Todo item has been completed!'})

# lets current user delete todo


@app.route('/todo/<todo_id>', methods=['DELETE'])
@token_required
def delete_todo(current_user, todo_id):
    todo = Todo.query.filter_by(
        id=todo_id, user_id=current_user.id).first()
    if not todo:
        return jsonify({'message': 'No todo found!'})
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'message': 'Todo item deleted!'})


if __name__ == '__main__':
    app.run(debug=True)

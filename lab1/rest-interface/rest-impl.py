from flask import Flask, jsonify, request
from serialization import common
from logic import budget
import os

app = Flask(__name__)


@app.route('/budget/<name>', methods=['GET'])
def get_user(name):
    user = common.load_user(name)
    return jsonify(user.get_owner(), user.get_total())


@app.route('/budget/<name>/stat', methods=['GET'])
def get_user_stat(name):
    return jsonify(common.load_user(name).get_statistic())


@app.route('/budget/<name>', methods=['POST'])
def post_user(name):
    for root, dirs, files in os.walk("../user-json/"):
        for filename in files:
            if str(name + ".json") == filename:
                return jsonify({'result': None})
    user = budget.Budget(request.args.get('total'), name)
    common.save_user(user)
    return jsonify(user.get_owner(), user.get_total(), user.get_statistic())


@app.route('/budget/<name>', methods=['DELETE'])
def delete_task(name):
    os.remove('../user-json/' + name + '.json')
    os.remove('../user-json/' + name + '_stat.json')
    return jsonify({'result': True})


@app.route('/', methods=['GET'])
def hello():
    return 'Hello, welcome to the budget controller!'


@app.route('/budget/<name>', methods=['PUT'])
def update_user(name):
    user = None
    for root, dirs, files in os.walk("../user-json/"):
        for filename in files:
            if str(name + ".json") == filename:
                user = common.load_user(name)
    if user is not None:
        user.set_owner(request.args.get('user_name'))
        os.remove('../user-json/' + name + '.json')
        os.remove('../user-json/' + name + '_stat.json')
        common.save_user(user)
        return jsonify(user.get_owner(), user.get_total(), user.get_statistic())
    else:
        return jsonify({'result': None})


if __name__ == '__main__':
    app.run()

from flask import Flask
from serialization import common

app = Flask(__name__)


@app.route('budget/new/user', methods=['POST'])
def post_user(budget_obj):
    return common.load_user()


@app.route('budget/all', methods=['GET'])
def get_all_stat():
    return 'ALL'


@app.route('/budget/user/stat', methods=['GET'])
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

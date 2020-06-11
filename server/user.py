import sqlite3
from flask import jsonify
from flask_restx import Namespace, Resource

api = Namespace('users', description='User resources')

parser = api.parser()
parser.add_argument("name", type=str, required=True, help="The user name")

#---------------------------------------------------------------------------
@api.route('/users/<int:user_id>')
@api.param('user_id', description='User ID')
class User(Resource):
    def get(self, user_id=None):
        """ Возвращает пользователя с запрошенным id в формате Json """
        db = sqlite3.connect('db.sqlite')
        c = db.cursor()
        if user_id:
            c.execute("select name from appuser where id = ?", (user_id,))
            for name, in c:
                return jsonify(id=user_id, name=name)
            return "User not found", 404


@api.route('/users/')
class Users(Resource):
    def get(self):
        """ Возвращает список пользователей в формате Json """
        users = list()
        db = sqlite3.connect('db.sqlite')
        c = db.cursor()
        c.execute("select * from appuser")

        for user_id, name in c:
            users.append(dict(id=user_id, name=name))
        return jsonify(users)

    @api.doc(parser=parser)
    def post(self):
        """ Добавление нового пользователя в БД """
        args = parser.parse_args()
        db = sqlite3.connect('db.sqlite')
        c = db.cursor()
        user_id = self.max_id() + 1
        c.execute("INSERT INTO appuser VALUES (?, ?)", (user_id, args['name']))
        db.commit()
        return user_id, 201

    @staticmethod
    def max_id():
        """ Нахождение максимального текущего id пользователя """
        db = sqlite3.connect('db.sqlite')
        c = db.cursor()
        c.execute("select max(id) from appuser")
        mid = c.fetchone()[0]
        return mid

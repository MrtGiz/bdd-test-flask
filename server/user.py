import sqlite3
from sqlite3 import Error
from flask import jsonify
from flask_restx import Namespace, Resource

DB_FILE = 'db.sqlite'

api = Namespace('users', description='User resources')

parser = api.parser()
parser.add_argument("name", type=str, required=True, help="The user name")


@api.route('/users/<int:user_id>')
@api.param('user_id', description='User ID')
class User(Resource):

    def get(self, user_id=None):
        """ Возвращает пользователя с запрошенным id в формате Json """
        db = create_connection(DB_FILE)
        c = db.cursor()
        if user_id:
            c.execute("select name from appuser where id = ?", (user_id,))

            try:
                name = c.fetchone()[0]
                return jsonify(id=user_id, name=name)
            except Exception as err:
                print(err)
                return "User not found", 404
            finally:
                db.close()


@api.route('/users/')
class Users(Resource):

    def get(self):
        """ Возвращает список пользователей в формате Json """
        users = list()
        db = create_connection(DB_FILE)
        c = db.cursor()
        c.execute("select * from appuser")

        for user_id, name in c:
            users.append(dict(id=user_id, name=name))
        db.close()
        return jsonify(users)

    @api.doc(parser=parser)
    def post(self):
        """ Добавляет нового пользователя в БД """
        args = parser.parse_args()
        db = create_connection(DB_FILE)
        c = db.cursor()

        new_user_id = self.max_id(db) + 1
        c.execute("INSERT INTO appuser VALUES (?, ?)", (new_user_id, args['name']))
        db.commit()
        db.close()
        return new_user_id, 201

    @staticmethod
    def max_id(conn):
        """ Нахождение максимального текущего id пользователя """
        c = conn.cursor()
        c.execute("select max(id) from appuser")
        max_id = c.fetchone()[0]
        return max_id


def create_connection(db_file):
    """ создает соединение с базой данных SQLite, указанной в db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

        return conn

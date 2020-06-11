## Тестовое задание REST API

### Установка
```sh
# Создание папки проекта
$ mkdir flask-rest
$ cd flask-rest

# Создание виртуального окружения
$ virtualenv venv
$ source venv/bin/activate

# Клонирование репозитория
$ git clone https://github.com/MrtGiz/bdd-test-flask.git
$ cd bdd-test-flask

# Установка зависимостей
$ pip install -r requirements.txt

# Запуск проекта
$ python3 run.py
```


### Описание API

Users

HTTP-метод | Ресурс | Описание |
--- | --- | --- |
GET | /api/users/<int:user_id> | Получить пользователя с запрашиваемым id
GET | /api/users/ | Получить список пользователей |
POST | /api/users/ | Создание пользователя |

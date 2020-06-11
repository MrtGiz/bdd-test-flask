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
$ git clone https://github.com/X1Zeth2X/flask-restx-boilerplate.git

# Установка зависимостей
$ pip install requirements.txt

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

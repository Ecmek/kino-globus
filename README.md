# Проект kino-globus
## Киноафиша.
### Технологии
Python
Django
Bootstrap
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
cd kino-globus
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```
В корневой папке создать файл .env и заполнить согласно файла env_template.txt:
- Если на вашем пк не установлн какой-либо сервер с БД, то DATABASES изменить на пример ниже:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

Выполнить миграции:

```
python3 manage.py migrate
```
Создать суперюзера:

```
python3 manage.py createsuperuser
```
Соберите статику:

```
python3 manage.py collectstatic
```
Запустить проект:

```
python3 manage.py runserver
```
Авторизоваться на сайте:
```
/admin/login
```
После чего на главной странице, либо через адмим-панель можно добавить киноленты и сеасны к ним.

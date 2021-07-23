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

Выполнить миграции:

```
python3 manage.py migrate
```
Создать суперюзера:

```
python3 manage.py createsuperuser
```

Запустить проект:

```
python3 manage.py runserver
```
Авторизоваться на сайте:
```
/admin/login
```
После чего на главной странице, либо через админим панель можно добавить киноленты и сеасны к ним.

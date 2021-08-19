Для разворота проекта необходимо проделать ряд действий:

```bash
$ git clone https://github.com/sandanilenko/peerocks.git
$ cd peerocks
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt -r requirements-dev.txt
$ cd peerocks
$ python manage.py migrate
$ python manage.py prepare_db
```

После выполнения команд будет получена подготовленный проект и его база для работы.
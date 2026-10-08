# Django проект

Базовый Django проект с первым приложением `demoapp`, отображающим приветственную страницу.

Создан на основе стандартной команды:

```bash
django-admin startproject mysite .
python manage.py startapp demoapp
```

## Что реализовано

-  **Задача 2**: Стандартный Django-проект (миграции, сервер запускается, системная проверка проходит без ошибок).
-  **Задача 3**: Первое приложение `demoapp` с приветственной страницей:
  - По адресу `http://127.0.0.1:8000/` отображается **"Привет из Django!"** и текущее время на сервере.
  - Маршруты приложения подключены через `include()` в `mysite/urls.py`.
  - Приложение зарегистрировано в `INSTALLED_APPS` в `mysite/settings.py`.

## Требования

- Python 3.10+
- pip
- Git

## Установка и запуск

1. Клонируйте репозиторий:

```bash
git clone <URL_репозитория>
cd <имя_папки>
```

2. Создайте виртуальное окружение:

```bash
python -m venv venv
```

3. Активируйте виртуальное окружение:

- Windows:
  ```bash
  venv\Scripts\activate
  ```
- macOS / Linux:
  ```bash
  source venv/bin/activate
  ```

4. Установите зависимости:

```bash
pip install -r requirements.txt
```

5. Выполните миграции:

```bash
python manage.py migrate
```

6. Запустите сервер разработки:

```bash
python manage.py runserver
```

7. Откройте в браузере:

- Приветственная страница (Задача 3): http://127.0.0.1:8000
- Панель администратора: http://127.0.0.1:8000/admin

## Структура проекта

```
Django_проект/
├── manage.py               # Утилита управления Django
├── mysite/                 # Пакет проекта с настройками
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py             # Главные маршруты (подключают demoapp)
│   └── wsgi.py
├── demoapp/                # Первое приложение (Задача 3)
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py             # Маршруты приложения
│   └── views.py            # Представление home()
├── requirements.txt        # Зависимости проекта
├── .gitignore              # Правила игнорирования для Git
└── README.md               # Эта инструкция
```

## Проверка работоспособности

```bash
python manage.py check
# System check identified no issues (0 silenced).

python manage.py runserver
# Откройте http://127.0.0.1:8000 — должна появиться страница
# с надписью "Привет из Django! 👋".
```

## Автор

Чжэн Дунлинь 2-МГ-2

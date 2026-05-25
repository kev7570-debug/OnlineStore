# OnlineStore

Интернет-магазин для продажи цифровых товаров (плагины, скрипты, утилиты).

## Описание проекта

Проект интернет-магазина, который разрабатывается в рамках курса по Django. 
На данный момент реализованы главная страница и страница с контактами.

## Установка и запуск

### 1. Клонируйте репозиторий

git clone <https://github.com/kev7570-debug/OnlineStore>
cd Djangohomework_2


### 2. Создайте и активируйте виртуальное окружение
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

### 3. Установите зависимости
pip install -r requirements.txt

### 4. Выполните миграции
python manage.py migrate

### 5. Запустите сервер
python manage.py runserver

### 6. Откройте в браузере
Главная страница: http://127.0.0.1:8000/

Контакты: http://127.0.0.1:8000/contacts/

#### Технологии
Python 3.x
Django 5.x
Bootstrap 5
SQLite

##### Структура проекта
Djangohomework_2/
│
├── catalog/                     # Приложение каталога
│   ├── migrations/              # Миграции базы данных
│   │   └── __init__.py
│   ├── templates/               # Шаблоны HTML
│   │   └── catalog/
│   │       ├── home.html        # Главная страница
│   │       └── contacts.html    # Страница контактов
│   ├── __init__.py              # Инициализация приложения
│   ├── admin.py                 # Настройка админ-панели
│   ├── apps.py                  # Конфигурация приложения
│   ├── models.py                # Модели данных
│   ├── tests.py                 # Тесты
│   ├── urls.py                  # Маршруты приложения
│   └── views.py                 # Контроллеры (логика)
│
├── config/                      # Настройки проекта
│   ├── __init__.py
│   ├── settings.py              # Основные настройки Django
│   ├── urls.py                  # Главные маршруты
│   ├── asgi.py
│   └── wsgi.py
│
├── venv/                        # Виртуальное окружение
├── .gitignore                   # Игнорируемые файлы для Git
├── db.sqlite3                   # База данных SQLite
├── manage.py                    # Управляющий скрипт Django
├── README.md                    # Описание проекта
└── requirements.txt             # Зависимости проекта


###### Автор
[Elena Kashina]

###### Статус
В разработке

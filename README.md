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
├── catalog/          # приложение каталога
│   ├── templates/    # HTML-шаблоны
│   ├── views.py      # контроллеры
│   └── urls.py       # маршруты приложения
├── config/           # настройки проекта
├── venv/             # виртуальное окружение
├── manage.py
├── requirements.txt
└── README.md

###### Автор
[Elena Kashina]

###### Статус
В разработке
# Система управления вещами (бэкенд)

Система хранения личных вещей пользователя. 

Создает список личных вещей пользователя. Фильтр вещей по категориям и местам хранения.
Сохраняет в базу: фото, название, описание, категория, место хранения.

## Установка

1. Склонируйте репозиторий 

```
git clone https://github.com/ardash-ds/user-belongings-management.git
```

2. Установите виртуальное окружение и активируйие его


Для windows:
```
python -m venv venv
venv\scripts\activate
```

Для linux:
```
python3 -m venv venv
source venv/bin/activate
```

3. Установите зависимости

```
pip install -r requirements.txt
```

4. Добавьте в корень проекта файл с переменными окружения .env

```
Заполните переменными файл .env_blank и переименуйте его в .env
```

5. Сделайте миграции

```
python manage.py makemigrations categories items storage users
python manage.py migrate
```

6. Заполните бд тестовыми данными

```
python manage.py entity_population
```

7. Запуск сервера

```
python manage.py runserver
```

8. Запуск юнит-тестов 

```
python manage.py test
```

9. Создание суперпользователя для доступа в админку

```
python manage.py createsuperuser
```

Адрес свагера: [http://127.0.0.1:8000/docs/]

Админка: [http://127.0.0.1:8000/admin/]

## Архитектура

Архитектура этого проекта представляет собой стандартную архитектуру Django, реорганизованную в соответствии с принципами **DDD**, где каждый раздел приложения строго связан с другим.

Единственное **отклонение** от архитектуры, основанной на **DDD**, появляется в папке **"serializers"**, где сериализаторы разделены на **model**, **request** и **response**.

```
categories
├── core
│   └──  categories.py
│
├── models
│   └──  categories.py
│
├── urls
│   └──  categories.py
│
├── views
│   └──  categories.py
│ 
├── serializers
│   ├──  model.py
│   ├──  request.py
│   └──  response.py
│
└── tests
    └──  test_get_categories.py

```

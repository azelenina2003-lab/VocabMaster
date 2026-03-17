# Установка и настройка

## Требования
- Python 3.10 или выше
- pip (менеджер пакетов)
- Виртуальное окружение (рекомендуется)

## Инструкция

### 1. Клонируйте репозиторий
*bash:*
git clone <url-репозитория>
cd flashcard_project

### 2. Создайте и активируйте виртуальное окружение
*Windows:*
python -m venv venv
venv\Scripts\activate

*Mac / Linux:*
python3 -m venv venv
source venv/bin/activate

### 3. Установите зависимости
*Вы должны находиться в корневой папке, после чего выполнить команду:*
pip install -r requirements.txt
 *Если файла requirements.txt нет,то создайте его и заполните следующим образом:*
Django==6.0.3
pytest
pytest-django
factory-boy
Faker

### 4. Применените миграции
python manage.py migrate

### Создаqnt суперпользователя 
python manage.py createsuperuser
*Придумайте имя пользователя, введите e-mail, придумайте пароль*

### 6. Запустите сервер 
python manage.py runserver
*Сервер будет доступен по адресу http://127.0.0.1:8000/*.

### 7. Перейдите по ссылке

*Если установка прошла успешно, Вы попадёте на стартовую страницу проекта*

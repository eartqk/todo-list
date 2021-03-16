# todo-list
Приложение todo-list    

Фронтенд на чистом JS  
Бэкенд на Django REST API

#### Методы на бэкенде:
- /api/ - [GET] - Показывает список доступных методов
- /api/task-list/ - [GET] - Возвращает список элементов
- /api/task-detail/\<pk\>/ - [GET] - Возвращает элемент по id
- /api/task-create/ - [POST] - Принимает элемент
- /api/task-update/\<pk\>/ - [POST] - Обновляет элемент по id
- /api/task-delete/\<pk\>/ - [DELETE] - Удаляет элемент по id

#### Запуск:  
Склонируйте репозиторий и перейдите в папку с ним
```
git clone https://github.com/eartqk/todo-list
cd todo-list
```
Создайте виртуальное окружение для Python и установите все зависимости*
```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```
Проведите миграцию
```
python manage.py makemigrations
python manage.py migrate
```
Запустите
```
python manage.py runserver
```
\*необязательно создавать виртуальное окружение, однако, так пакеты будут установлены только в этой среде и не будут влиять глобально.

#### Внешний вид:
![image](https://i.snipboard.io/4mZPqt.jpg)

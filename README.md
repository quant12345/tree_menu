# Запуск на локальном сервере

1. Клонируйте репозиторий и перейдите в него: 

```
https://github.com/quant12345/tree_menu.git
```

или скачайте папку **tree_menu** и перейдите в нее:

```
cd 'ваш путь вплоть до папки'
```

2. Установите и активируйте виртуальное окружение: 
```
python -m venv venv
```
```
source venv/Scripts/activate
```
3. Установите зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
4. Выполните миграции:
```
python manage.py migrate
```
5. Создайте суперпользователя:
```
python manage.py createsuperuser
```
6. Запустите сервер:
```
python manage.py runserver
```
7. В админ панели создайте записи(пункты), если это необходимо(в проекте уже есть записи в файле db.sqlite3). Пример ниже, после гиф анимации.
![](https://github.com/quant12345/tree_menu/blob/master/imgs/display.gif)
![](https://github.com/quant12345/tree_menu/blob/master/imgs/database.jpg)





ДЗ 8. Django model form

Выполнять в текущем проекте или создать новый (не забываем про flake8)
Создать новую модель с несколькими полями. Создать миграцию и мигрировать.

Person
first_name - charfield
last_name - charfield
email - emailfield

Создать modelform, view, template для - создания новой записи, и для редактирования существующей записи.

/person - GET - получить форму
/person - POST - отвалидировать и сохранить новый объект Person в базу

/person/<id:int> - GET - получить форму с данными Person, или 404 если пользователя с таким id не существует
/person/<id:int> - POST - обновить данные Person, или 404

используйте instance= для инициализации формы с данными person
используйте get_or_404 для того что бы быстро получить Person или вызвать ошибку

https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/#get-object-or-404


ДЗ 7. Django forms на базе проекта Django (ДЗ 6)

Добавить вью по пути /triangle

На этой вью необходимо использовать форму которая будет принимать значения двух катетов треугольника (положительные, больше нуля, для простоты используйте int значения если хотите). После отправки формы, если значения были валидными - на этой же странице вывести значение гипотенузы.


ДЗ 6 queryset filter, managment commands на базе проекта Django (ДЗ 5)

Написать кастомную менеджент комманду которая будет генеритовать случайных пользователей ( https://docs.djangoproject.com/en/3.2/ref/models/querysets/#create ) c username, email и password. 
Команда принимает один обязательный аргумент - количество вновь сгенерированных пользователей. 
Значения меньше 1 и больше 10 - должны вызывать ошибку.

https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/


ДЗ 5 Flake8, Travis CI на базе проекта Django (ДЗ 4)

В текущий репозиторий, или в новый django проект добавить flake8 с дополнительными модулями (flake8-django, flake8-import-order, flake8-builtins, flake8-print).
Настроить файл конфигураций для него и проверить свой код на предмет ошибок. исправить их.

Зарегистрироваться на travis ci и добавить интеграцию в github. добавить файл настроек для этого-же и настроить его так, что бы новый коммит проверялся flake8 средствами travis ci.


ДЗ 4 Django tutorial:

Выполнить все следующие шаги туториала

https://docs.djangoproject.com/en/3.2/intro/tutorial01/
https://docs.djangoproject.com/en/3.2/intro/tutorial02/
https://docs.djangoproject.com/en/3.2/intro/tutorial03/
https://docs.djangoproject.com/en/3.2/intro/tutorial04/
https://docs.djangoproject.com/en/3.2/intro/tutorial05/
https://docs.djangoproject.com/en/3.2/intro/tutorial06/
https://docs.djangoproject.com/en/3.2/intro/tutorial07/

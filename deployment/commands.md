## Some important commands

Start sever
```
python manage.py runserver
```
Update db after structure change
```
python manage.py makemigrations
python manage.py migrate --noinput
```

Update language file
* First create updated django.po ```django-admin makemessages -l de```
* Update the translations
* compile the file for usage ```django-admin compilemessages```
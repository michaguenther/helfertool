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
<<<<<<< HEAD
* compile the file for usage ```django-admin compilemessages```
=======
* compile the file for usage ```django-admin compilemessages```

Change admin passwort:

    python manage.py changepassword
>>>>>>> 5c076aab6e06f1edbef1f810af72f60d4429fe2b

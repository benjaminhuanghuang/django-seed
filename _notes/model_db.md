## Db configration in settings.py
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

## Install DB Browser for SQLite
    - http://sqlitebrowser.org/

## Create Django model in app/models.py
    class Items(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField()
        quantity = models.IntegerField()
        
## Data type
<img src='https://github.com/benjaminhuanghuang/django-seed/blob/master/_notes/data_type.png' title='data type' width='' alt='data type' />


## Migration
    Auto generates scripts to amend the database
    $ python manage.py makemigrations   # init migration, generate migration files
    $ python manage.py migrate          # run all migrations to create table "django_app_items"in db
    
## Register Item, ItemsAdmin and setup Admin account
    - Register Item in admin.py
    - Create admin user
        $ python manage.py createsuperuser 
    - Login as admin
        http://localhost:8000/admin
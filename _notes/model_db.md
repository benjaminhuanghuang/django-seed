## Install DB Browser for SQLite


## Create Django model in app/models.py
    class Items(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField()
        quantity = models.IntegerField()
        
## Data type
<img src='https://github.com/benjaminhuanghuang/django-seed/blob/master/_notes/data_type.png' title='data type' width='' alt='data type' />


## Migration
    Auto generates scripts to amend the database
    $ python manage.py makemigrations   # generate migration files
    $ python manage.py migrate          # run all migrations
    
    

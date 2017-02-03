Django Project Template
=====================================
Code to demonstrate 

- Project template for Django Project.

Requirements
------------

- Python 2.7 or 
- virtualenv 
- git
- Network connection (only to install the application)

Setup
-----

**Step 1**: Clone the git repository

    $ git clone https://github.com/benjaminhuanghuang/djangoTemplate.git
    $ cd rest_bank_project

**Step 2**: Create a virtual environment.

For python2 :

    $ virtualenv venv
    $ source venv/bin/activate
    (venv) $ pip install -r requirements.txt

For python3 :

    $ brew install python3
    $ pyvenv venv3
    $ source venv3/bin/activate
    (venv) $ pip install -r requirements.txt

**Step 3**: Create project.
    $ django-admin.py startproject my_blog
    $ python manage.py startapp article
    
**Step 4**: Start Server.
    $ python manage.py runserver
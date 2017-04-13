<project_name>
    <project_name>
        __init__.py      # used to make package and notify django of the project
        settings.py      # configure project
        urls.py          # configure the routes
        wsgi.py          # used by a web server to run the project
    
    <app_name>
        <migrations>
        __init__.py      # 
        admin.py         # admin interface to manage app
        apps.py          # app files
        models.py        # defines database structure
        tests.py         # automated tests   
        views.py         # determines the program logic
        
    Db.sqlite3
    manage.py            # run commands for the project
    
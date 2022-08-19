# student-record-mgmt
# Setting up database
    -Go to /student_mgmt/student_mgmt/settings.py and make changes in data base confoguration shown as below
    <pre>
    DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME':  BASE_DIR / 'student_db',
        }
    }
    </pre>
    Run these commannds for creating database
    $ cd student_mgmt
    $ python manage.py makemigrations
    $ python manage.py migrate

# Cretaing virtual env and installing packages
    -This is one time steup
    $ virtualenv env
    
    $ source env/bin/activate(linux)

    $ .\env\Scripts\activate(windows)

    $ pip install -r requirements.txt
        
# Running application
    $ cd student_mgmt
    $ python manage.py runserver

# college-mgmt-system
# Setting up database
    -Go to /college_mgmt/college_mgmt/settings.py and make changes in data base confoguration shown as below
    <pre>
    DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME':  BASE_DIR / 'student_db',
        }
    }
    </pre>
    Run these commannds for creating database
    $ cd college_mgmt
    $ python manage.py makemigrations
    $ python manage.py migrate

# Cretaing virtual env and installing packages
    -This is one time steup
    $ virtualenv env
    
    $ source env/bin/activate(linux)

    $ .\env\Scripts\activate(windows)

    $ pip install -r requirements.txt
        
# Running application
    $ cd college_mgmt
    $ python manage.py runserver


<h1>Screenshots</h1>

![Home page](https://user-images.githubusercontent.com/97660344/188319725-20f0d451-9823-4631-a965-12c93bd87bb4.PNG)
<p>fig 1: Home Page </p></br>

![signup](https://user-images.githubusercontent.com/97660344/188319782-bc19f42c-d13d-4395-ab36-e538d41b2f85.PNG)
<p>fig 2: Signup Page </p></br>

![login](https://user-images.githubusercontent.com/97660344/188319807-7442490f-6c62-4e8c-8113-15e8fff04872.PNG)
<p>fig 3: Login Page </p></br>

![student crud](https://user-images.githubusercontent.com/97660344/188322117-19fc54f8-bab9-406e-b463-dbd02b337435.PNG)
<p>fig 4: Student CRUD Table in Admin Page </p></br>

![teacher crud](https://user-images.githubusercontent.com/97660344/188322143-35921543-af29-46e9-adcc-dfdf7e4cf72e.PNG)
<p>fig 5: Teacher CRUD Table in Admin Page </p></br>

![admin home](https://user-images.githubusercontent.com/97660344/188892602-ef081a69-0a44-4fce-93d1-fa2fc75b0849.PNG)
<p>fig 6: Admin Home Page </p></br>

![student dashboard](https://user-images.githubusercontent.com/97660344/188893032-1f19b2fb-bcaf-4a5e-a3fb-8b70f2ae71b4.PNG)
<p>fig 7: Student Home Dashboard </p></br>

![assignment submission](https://user-images.githubusercontent.com/97660344/189114854-7e151c48-8149-46e2-b793-d5411da763b4.PNG)
<p>fig 8:Student Assignment Submission Page </p></br>

![teacher dashboard](https://user-images.githubusercontent.com/97660344/188893430-6818b9a9-510d-4716-970e-d1ad0f7cd6c5.PNG)
<p>fig 9: Teacher Dashboard </p></br>

![create assignment modal](https://user-images.githubusercontent.com/97660344/189114654-28f56574-a9e1-4366-9cf6-70f24daa43c3.PNG)
<p>fig 10: Create Assignment</p></br>

![about cms](https://user-images.githubusercontent.com/97660344/189114774-435e810f-76b6-4352-b7c3-dfb4ee14369d.PNG)
<p>fig 11: About Page(About CMS) </p></br>

![about college](https://user-images.githubusercontent.com/97660344/189114943-d5fc4763-5bec-4d3d-835d-702ec9902645.PNG)
<p>fig 12: About Page(About College) </p></br>

![about team](https://user-images.githubusercontent.com/97660344/189115097-6573fce1-0c09-4555-bf87-890902fdb4b4.PNG)
<p>fig 13: About Page(About Team) </p></br>

![contact](https://user-images.githubusercontent.com/97660344/189115029-bb63edc6-a9ce-409c-bb9b-d675cee017f3.PNG)
<p>fig 14: Contact Page </p></br>



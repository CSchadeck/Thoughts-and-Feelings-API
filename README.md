Resting API for Feelings Forum or Post related website

Languages: Python + Django

***LOCAL SERVER  ACTIVATION***
Run the server in the terminal  with command: python manage.py runserver

***WORKING ENVIRONMENT***
The active files for editing the API is in the .venv folder. 

1. from the main director CD down to the .venv folder
2.This will open the virtual environment.
3. CD ino the Thoughts folder to find all files for configuration of the api:
models.py = setting up structure and data types for the Thought table/data storage.

serializers.py = files to configure serializer to support conversion to json. 

settings.py = includes all projects dependencies, middleware configuration, and paths.

urls.py = url path specificity.

views.py = configuration of crud and data access.

4. db.sqlite3 = table transfer for the Thought table as well as Django table add on for admin configuration.  

***RESOURCES**
Python Full course for Beginners with Mosh Hamedani-https://youtu.be/_uQrJ0TkZlc

Django REST Framework-Build an API from scratch with Caleb Curry- https://youtu.be/i5JykvxUk_A

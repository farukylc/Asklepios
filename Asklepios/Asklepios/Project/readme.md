## Asklepios Webapp

This folder contains the webapp which created with Django. 

To run app you should relocate the path which contains manage.py folder then you should run 
"python manage.py runserver 0.0.0.0:8080" command.

This app responsible from:
* User Authentication
* Communication with API
* Store the Database
* Admin Panel

## 📦 To download necessary libraries run these command on your terminal:

* pip install tensorflow
* pip install numpy
* pip install pandas
* pip install matplotlib
* pip install django

## Important Note:
❗️❗️❗️It's important to note that when running the Django server for the WebApp, both the API and the WebApp should be assigned to different ports to avoid conflicts.When starting the servers, ensure that you specify distinct ports for each of them. For example, you can run the API server on port 8000 and the Django server for the WebApp on a separate port like 8080. This separation allows both servers to coexist and function independently without interfering with each other.
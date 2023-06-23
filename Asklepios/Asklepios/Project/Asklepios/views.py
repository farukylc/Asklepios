from django.shortcuts import render, redirect
import os
from django.conf import settings
from .models import *
import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import django
from django.contrib.auth.models import User

# Login function

def login(request):
    if request.method == 'POST':
       login_username =  request.POST["login_username"]
       login_password = request.POST["login_password"]

       user = authenticate(request, username=login_username, password = login_password)
       
       if user  is not None:
           django.contrib.auth.login(request, user) 
          
           return redirect('upload_page')
       else:
           return render(request, "login.html",{'error':'Username or Password is incorrect', 
                                                })
    
    return render(request,'login.html')

# Register 
def register(request):
    if request.method == 'POST':
        new_register = User.objects.create_user(request.POST["register_username"], "", request.POST["register_password"])
        new_register.save()
        return redirect('/')

    return render(request, 'register.html')


@login_required(login_url="/")
def upload_page(request): #This line defines a function named upload_page that takes a request 
                         #parameter. This function is likely a view function in a Django web application.
   

    if request.method == 'POST': #This line checks if the HTTP method of the request is POST. In Django, 
                                 #when a form is submitted, the browser sends a POST request to the server.


        
        uploaded_file = request.FILES['exampleFormControlFile1'] #This line retrieves the file uploaded by the user from the request. 
                                                                 #exampleFormControlFile1 is the name of the file input field in the 
                                                                 # HTML form. The uploaded file is stored in the uploaded_file variable.
        
        file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name) #This line constructs the file path where the 
                                                                         #uploaded file will be saved. 
                                                                         #It uses the MEDIA_ROOT setting from Django's settings and 
                                                                         # appends the name of the uploaded file.
        
        with open(file_path, 'wb') as file: #This line opens a file in binary write mode ('wb') with the file path 
                                            #obtained earlier. It uses a with statement to ensure that the file is properly closed after use
            
            for chunk in uploaded_file.chunks(): #This loop iterates over the chunks of the uploaded file and writes each chunk to the opened file. 
                                                #It allows for efficient handling of large files by processing the file in smaller pieces
                file.write(chunk)
        
        result = request_from_api(file_path) #This line calls a function named request_from_api and passes the file_path as an argument.
                                            #It sends the file to an API for processing and returns a result.
        newUpload = UploadImage(
             #This line creates a new instance of the UploadImage model (assuming it exists) 
             #with the provided data. It assigns the values of name and surname from the corresponding 
             #fields in the submitted form. image is set to the uploaded file, 
             #and result is set to the result obtained from the API.
            
            name = str(request.POST['first_name']), 
            surname = str(request.POST['surname']),
            image = uploaded_file,
            result = result
        )
        newUpload.save()
        return redirect('upload_page')
   

    user_data = UploadImage.objects.all

    data = {
        "user_datas": user_data
    }

    return render(request, 'upload_page.html',data)


def request_from_api(path):
    payload = {"path": path}
    result = requests.get('http://127.0.0.1:8000/cnn',params=payload)
    return result.text



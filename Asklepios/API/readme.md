## Asklepios API 

The provided script is the API script of the project, which has been developed using FastAPI, a Python web framework.

## 📦 To ensure that FastAPI is installed on your system, please run the following commands in your terminal:

* pip install fastapi
* pip install uvicorn

Once FastAPI is installed, you can run the API by executing the command
* uvicorn cnnAPI:app --reload

## 📦 To download other necessary libraries:

* pip install tensorflow
* pip install numpy
* pip install pandas
* pip install matplotlib

## Important Note:
❗️❗️❗️It's important to note that when running the Django server for the WebApp, both the API and the WebApp should be assigned to different ports to avoid conflicts.When starting the servers, ensure that you specify distinct ports for each of them. For example, you can run the API server on port 8000 and the Django server for the WebApp on a separate port like 8080. This separation allows both servers to coexist and function independently without interfering with each other.
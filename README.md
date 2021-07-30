# Salary-Predictor-App
This is a salary prediction application for tech roles and was developed in Jupyter notebook with PYTHON, wrapped in FLASK API, and then deployed on Heroku (A Platform as a Service -PaaS).

The application requests input features from users through the HTML form, makes a prediction with its Machine Learning model, and then outputs the result back to the user.

## Files
1. requirements.txt -this file contains all the external modules used in the development of the application. To get a requirements.txt file for your model, 
open the command prompt on your computer, cd into the Folder/Directory where your files are, then enter the following command: 'pip freeze > requirements.txt'

2. salary_app2 -this is the model's API created with FLASK. It consists of the machine learning model and some processes to enable smooth transfer between 
the user interface and the model. We can call it a mini backend of the application.

3. Procfile -this file contains three pieces of information written in a simple format and it serves as the interface between our python code and the Heroku platform.
 
   application type, server information, and application name (where the application should start running from)

4. index.html -this is a web interface through which the user interacts with the model.

5. Model.pkl -this is a serialized form of our machine learning model.


## Folders
1. Notebooks -The notebooks show how the Machine learning model (the business logic), Flask API, and User Interface were built.

2. templates -This folder contains the index.html file.


## Developer
Jahfaith Irokanulo

Data Scientist/DevOps Engineer.

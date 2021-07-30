#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import required packages
from flask import Flask, render_template, request, jsonify
import pickle


#create a Flask object
app = Flask("SALARY PREDICTION APP")

#load the ml model which we have saved earlier in .pkl format
model = pickle.load(open('Pace_Model.pkl', 'rb'))

#define the route(basically url) to which we need to send http request
#HTTP GET request method
@app.route('/',methods=['GET'])

#create a function Home that will return index.html(which contains html form)
#index.html file is created seperately
def Home():
    return render_template('index.html')

#HTTP POST request method
#define the route for post method 
@app.route("/predict", methods=['POST'])

#define the predict function which is going to predict the results from ml model based on the given values through html form
def predict():
    
    if request.method == 'POST':

        #Use request.form to get the data from html form through post method.
        #these are features of our salary dataset(ml model)
        
        Degree = bool(request.form['Degree'])
        Experience = int(request.form['Experience'])
        
        Company_location = str(request.form['Company_location'])
        #Company_location is categorised into America, Europe, Nigeria, and Africa. It was label encoded during model development, therefore, we will assign their codes to them to enable the api send the right message to the machine.
        if Company_location == 'America':
            Company_location = 0
        elif Company_location == 'Europe':
            Company_location = 1
        elif Company_location == 'Nigeria':
            Company_location = 2
        elif Company_location == 'Africa':
            Company_location = 3
            
        Title = str(request.form['Title'])
        #Job Title was grouped into Backend, Frontend, Devops and others as listed below. It was also label encoded with the below codes that are assigned to the titles.
        if Title == 'Backend':
            Title = 0
        elif Title == 'Data Engineer':
            Title = 2
        elif Title == 'DevOps':
            Title = 2
        elif Title == 'Data Scientist':
            Title = 1
        elif Title == 'Data Analyst':
            Title = 1
        elif Title == 'Frontend':
            Title = 3
        elif Title == 'Fullstack':
            Title = 4
        elif Title == 'IT':
            Title = 6
        elif Title == 'Product Designer':
            Title = 7
        elif Title == 'Software Engineer':
            Title = 8
        elif Title == 'Graphics Designer':
            Title = 5
        
        #Model Prediction.
        data = [[Degree, Experience, Company_location, Title]]
        sal = model.predict(data)
        
        #Recall that our target variable was also label encoded. '101k-200k' was encoded 0, '201k-300k' was encoded 1 during the model development. Hence,
        if sal==0:
            prediction='101k-200k'
        elif sal==1:
            prediction='201k-300k'
        elif sal==2:
            prediction='301k-400k'
        elif sal==3:
            prediction='401k-500k'
        elif sal==4:
            prediction='50k-100k'
        elif sal==5:
            prediction='<50k'
        elif sal==6:
            prediction='>500k'
        
        #Outputting the result.
        return render_template('index.html', prediction_text="Expected Salary Range is {}".format(prediction))
        
        
    #html form to be displayed on screen when no values are inserted; without any output or prediction.
    else:
        return render_template('index.html')


if __name__=="__main__":
    #run method starts our web service
    #Debug : as soon as I save anything in my structure, server should start again
    app.run(debug=True)






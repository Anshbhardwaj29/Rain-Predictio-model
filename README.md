# Rain Prediction Web App 🌦️
## Project Description

This web application uses a machine learning model to predict whether it will rain based on weather data input from the user. The model has been trained on weather features such as humidity, cloud cover, wind speed, and rainfall, and is integrated into the application using Flask.

The purpose of this project is to demonstrate a practical application of machine learning for rain forecasting, while providing a simple and user-friendly web interface.

## Why This Project?

To integrate a machine learning model with a web interface.
To build a practical, easy-to-use solution for rain prediction using live input data.
To showcase the usage of Flask for deploying machine learning models.
## Challenges & Future Improvements

Handling edge cases where input data might be incomplete or out-of-range.
Improving model accuracy with additional data and better feature engineering.
Potential future features include a live weather API integration for real-time predictions.
## Table of Contents
**Project Description**

**How to Install and Run the Project**

**How to Use the Project**

**Credits**

**How to Install and Run the Project
Prerequisites**

**To run this project locally, you'll need:**

Python 3.x, 
Flask: A lightweight Python web framework, 

NumPy: For numerical computations.

Pickle: To load the pre-trained machine learning model.

## Installation
**Clone the repository**:

bash
Copy code
**git clone [https://github.com/yourusername/weather-prediction-app.git](https://github.com/Anshbhardwaj29/Rain-Predictio-model.git)**
cd weather-prediction-app
Install the required Python packages:

bash
Copy code
**pip install -r requirements.txt**
Ensure you have the pre-trained machine learning model Classifier.pkl in the project directory.

**Start the Flask server:**

bash
Copy code
python app.py
**Open your browser and navigate to http://127.0.0.1:5000/.**

How to Use the Project
Once the web app is running, follow these steps:

**Enter the required weather data such as:**

Humidity3pm: The humidity percentage at 3 PM.

RainToday: Indicate if it rained today (1 for Yes, 0 for No).

Cloud3pm: Cloud cover at 3 PM on a scale.

Humidity9am: The humidity percentage at 9 AM.

Cloud9am: Cloud cover at 9 AM.

Rainfall: The amount of rainfall in mm.

WindGustSpeed: Wind gust speed in km/h.

Click the "Submit" button, and the application will predict if it will rain tomorrow based on the input data.

The result will be displayed, either indicating "Rain will be there!" or "No rain!".

## Example Screenshots
Include a screenshot of the form and the result page 
![App Screenshot]("C:\Users\ACER\Pictures\Screenshots\Screenshot (148).png")


Credits
Project Author: **Ansh Bhardwaj**


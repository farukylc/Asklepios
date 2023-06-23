#In these lines, the necessary libraries and modules are imported
from fastapi import FastAPI
import random
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing import image
from PIL import Image
import matplotlib.image as img

#An instance of the FastAPI class is created and assigned to the variable app. This will be used to define the API endpoints.
app = FastAPI()

# This line decorates the function pneumonia_detect with the @app.get("/cnn") decorator. 
# It means that when a GET request is made to the /cnn endpoint, the function pneumonia_detect will be executed.
@app.get("/cnn")
def pneumonia_detect(path:str):
   
    # This line loads a pre-trained Keras model using tf.keras.models.load_model function. 
    model = tf.keras.models.load_model('model')
    
    # These lines load the image specified by the path parameter using tf.keras.utils.load_img. 
    # The image is resized to a target size of (64, 64). Then, it is converted to a NumPy array using 
    # tf.keras.utils.img_to_array. Finally, np.expand_dims is used to add an extra dimension to the array 
    # to match the expected shape of the input for the model.
    test_image = tf.keras.utils.load_img(path, target_size = (64, 64))
    test_image = tf.keras.utils.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    
    # This line uses the loaded model to predict the class of the input image. 
    result = model.predict(test_image)
    


    # Based on the predicted probabilities, this if-else statement determines the class label for the image. 
    # If the probability of the first class is 0, it assigns the label 'Negative'. Otherwise, it assigns the label 'Positive (+)'
    if result[0][0] == 0:
        prediction = 'Negative'
    else:
        prediction = 'Positive (+)'
    
    return prediction




#uvicorn cnnAPI:app --reload
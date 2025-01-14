# Emotify
Recommending music based on your facial expressions using FER 2013 dataset and Sporify api


This Project is done by TEAM LXXXV  for our POSTMAN x API challenge hosted by Marwadi University 
1.SHAGUN TYAGI
2.ESHWAR ANAND BADUGU 
3.ARJUN MADATHIL MOOLAKARAN
4.SANJANA GAJAVELLI

# Project Description:
The emotion recognition model is trained on FER 2013 dataset. It can detect 7 emotions. The project works by getting live video feed from web cam, pass it through the model to get a prediction of emotion. Then according to the emotion predicted, the app will fetch playlist of songs from Spotify through spotipy wrapper and recommend the songs by displaying them on the screen.

# Features:
- Real time expression detection and song recommendations.
- Playlists fetched from Spotify using API.
- Neumorphism UI for website.

# Running the app:
Flask: 
- Run <code>pip install -r requirements.txt</code> to install all dependencies.
- In Spotipy.py enter your credentials generated by your Spotify Developer account in 'auth_manager'. Note: - This is only required if you want to update recommendation playlists. Also uncomment import statement in 'camera.py'.
- Run <code>python app.py</code> and give camera permission if asked.

# Tech Stack:
- Keras
- Tensorflow
- Spotipy
- Tkinter (For testing)
- Flask

# Dataset:
The dataset used for this project is the famous FER2013 dataset. Models trained on this dataset can classify 7 emotions. The dataset can be found <a href = "https://www.kaggle.com/msambare/fer2013">here</a>.


# Model Architecture:
- The model architecture is a sequential model consisting of Conv2d, Maxpool2d, Dropout and Dense layers:
1. Conv2D layers throughout the model have different filter size from 32 to 128, all with activation 'relu'
2. Pooling layers have pool size (2,2)
3. Dropout is set to 0.25 as anything above results in poor performance
4. Final Dense layer has 'softmax' activation for classifying 7 emotions
- Used 'categorical_crossentropy' for loss with 'Adam' optimizer with 'accuracy' metric


# Image Processing 
- The images were normalised, resized to (48,48) and converted to grayscale in batches of 64 with help of 'ImageDataGenerator' in Keras API.


# Current condition:
The entire project works perfectly fine. Live detection gives good frame rates due to multithreading.

# Project Components:
- Spotipy is a module for establishing connection to and getting tracks from Spotify using Spotipy wrapper.
- haarcascade is for face detection.
- camera.py is the module for video streaming, frame capturing, prediction and recommendation which are passed to main.py.
- main.py is the main flask application file.
- index.html in 'templates' directory is the web page for the application. Basic HTML and CSS.
- utils.py is an utility module for video streaming of web camera with threads to enable real time detection.
- train.py is the script for image processing and training the model.


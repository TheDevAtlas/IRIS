# Jacob McGowan 2021 #
# Control Script For Net #

# Imports For Data Display And Manipulation
import datetime as dt # The Date And Time
import numpy as np # Basic Functions
import pandas as pd # Data Manipulation And Translations
import matplotlib.pyplot as plt # Visualization

# Imports From The Web
import pandas_datareader as web # Yahoo Finance, World Bank, Ect

# Imports For Machine Learning
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

# Function For Creating A Bot #
def createABot():
    print("Create")
    # Ask For All Of Its Atrabutes
    # Create Basic Bot Outline
    # First Training (Needs To Be Short)
    # Save The Bot With A Name

# Function For Training A Bot #
def trainABot():
    print("Train")
    # Ask What Bot To Train (Print All Of The Bots Saved)
    # Recreate Bot In Code
    # Input Its Saved Settings (Load Old Training Into Bot Outline)
    # Ask What Company To Train Bot On
    # Ask What Dates To Train Bot On (Show Current Date And Date Company Openened)
    # Start A New Training To Modify Saved Settings
    # Save The Bot With New Settings Under Same Name

# Function For Running A Bot #
def runABot():
    print("Run")
    # Ask What Bot To Run (Print All Of The Bots Saved)
    # Recreate Bot In Code
    # Input Its Saved Settings (Load Old Training Into Bot Outline)
    # Ask What Company To Perform Prediction On
    # Ask What Dates To Use In Prediction
    # Ask How Far Into Future To Predict
    # Output Predictions In Graph And Text File And In Console

# Very Basic Menu For Navigation (Going To Be Replaced By Web Or Other Input) #
while True:
    
    # Print The Menu And Commands #
    print ("""
Welcome To IRIS

Please Enter A Command
1) "create" - Create a new bot
2) "train" - Train an existing bot
3) "run" - Run an existing bot
4) "end" - End the program
    """)

    # Take Input From User And Run Function Or Exit Program #
    selection = input("") 
    if selection =='create': 
      print("Creating A New Bot")
      createABot()
    elif selection == 'train': 
      print("Training An Existing Bot") 
      trainABot()
    elif selection == 'run':
      print("Using An Existing Bot") 
      runABot()
    elif selection == 'end': 
      break
    else: 
      print("Unknown Command") 
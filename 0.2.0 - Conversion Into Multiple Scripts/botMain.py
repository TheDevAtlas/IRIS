# Jacob McGowan 2021 #
# Control Script For Net #

import botManager as bm
bm.trainBot()

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
    # Call The createNewBot Function From botManager

# Function For Training A Bot #
def trainABot():
    print("Train")
    # Ask For The Bot Name
    # Ask For The Company ID
    # Ask For The Start Date
    # Ask For The End Date
    # Ask For Settings Of Training
    # Call The trainBot Function From botManager

# Function For Running A Bot #
def runABot():
    print("Run")
    # Ask For The Bot Name
    # Ask For The Company ID
    # Ask For How Many Days Into The Past
    # Ask For End Date
    # Ask For How Far Into Future
    # Call The runBot Function From botManager

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
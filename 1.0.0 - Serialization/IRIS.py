# Jacob McGowan 2021 #
# IRIS 1.0.0 Started August 6th, 2021 #

# Import packages #
import datetime as Datetime
import numpy as Numpy
import pandas as Pandas
import matplotlib.pyplot as Plot
import pandas_datareader as Web
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

def getData( ticker, startDate, endDate):
    # Get all data for a company between two dates
    StockData = Web.DataReader(ticker, 'yahoo', startDate, endDate)

    # Return normalized data for closing stock
    StockScale = MinMaxScaler(feature_range=(0,1))
    return StockScale.fit_transform(StockData['Close'].values.reshape(-1,1))

def prepData( data, prediction_days):
    # Init x_train and y_train lists
    x_train, y_train = [], []

    # Loop through data starting at prediction_days until the length of the data
    for x in range(prediction_days, len(data)):
        x_train.append(data[x-prediction_days:x,0])
        y_train.append(data[x,0])

    # Convert into numpy arrays and return data
    x_train, y_train = Numpy.array(x_train), Numpy.array(y_train)
    x_train = Numpy.reshape(x_train, (x_train.shape[0],x_train.shape[1],1))
    return x_train, y_train

def createModel( layers, unitsPerLayer, dropWeight):
    # Create model and add first layer with inputs
    model = Sequential()
    model.add(LSTM(units=unitsPerLayer,return_sequences=True,input_shape=(60,)))

    # Add layers and dropouts
    for x in range(layers-2):
        model.add(LSTM(units=unitsPerLayer))
        model.add(Dropout(dropWeight))

    # Create prediction layer
    model.add(Dense(units=1))

    # Compile the model and return it
    return model.compile(optimizer='adam',loss='mean_squared_error')

def trainModel( model, x_train, y_train, epochAmount, batch):
    # Train the model on data and return changes
    return model.fit(x_train,y_train,epochs=epochAmount,batch_size=batch)

#print(getData('FB',Datetime.datetime(2012,1,1),Datetime.datetime(2021,1,1)))
#print(prepData(getData('FB',Datetime.datetime(2012,1,1),Datetime.datetime(2021,1,1)),60))
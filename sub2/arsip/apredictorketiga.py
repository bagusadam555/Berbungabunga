#Importing the libraries and all of the functions
import pandas
import matplotlib.pyplot as plt
import random
import tensorflow as tf
import numpy
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from tensorflow.keras.optimizers import Adam

def sistem_predictor_losses_data(namafile,trainingulang):
 
    #Load the dataset
    dataset = pandas.read_csv(f'sub2/{namafile}')

    #DATA PREPROCESSING
    #Fix random seed for reproducibility

    numpy.random.seed(1)
    random.seed(1)
    tf.random.set_seed(1)

    #Importing the training set
    
    dataset_train = dataset.iloc[0:510, 2:6].values
    #Normalize the dataset
    scaler = MinMaxScaler(feature_range=(0, 1))
    dataset_train_scaled = scaler.fit_transform(dataset_train)
    #Convert an array of values into a dataset matrix
    trainX, trainY = [], []
    #Creates the xx timesteps of each value
    #Timesteps variations= 2,3,5
    for i in range(5, 510):
        #Contains the next value after the xx timesteps #Output= 4
        trainX.append(dataset_train_scaled[i-5:i, 0:4])
        #This is used to predict the next value (future value)
        trainY.append(dataset_train_scaled[i, 0:4])
    #Convert to numpy array to be accepted in our RNN
    trainX, trainY = numpy.array(trainX), numpy.array(trainY)
    #Reshape
    #Need to convert the array to a 3 dimension to be able to permit it into the RNN
    trainX = numpy.reshape(trainX, (trainX.shape[0],trainX.shape[1],4))
    #BUILDING THE RNN
    #Create and fit the LSTM network
    #Initialising the RNN
    model = Sequential()
    #Adding the input layer, the first LSTM layer and some Dropout regularisation
    #Jumlah unit neuron LSTM= 1, 5, 10, 20, 25
    model.add(LSTM(25, return_sequences=False, input_shape=(trainX.shape[1],4)))
    model.add(Dropout(0.2))
    #Adding the output layer
    model.add(Dense(4))
    #Compiling the RNN
    #Learning rate= 0.001, 0.005, 0.01, 0.1
    opt=Adam(learning_rate=0.01)
    model.compile(loss='mean_absolute_error', optimizer=opt)
    #Fitting the RNN to the training set
    if trainingulang==False: #False ngetraining ulang
        model.fit(trainX, trainY, epochs=30, batch_size=2)
        model.save("adam.h5")
    else:
        from tensorflow.keras.models import load_model
        model = load_model("adam.h5")
    
    #MAKING THE PREDICTIONS AND VALIDATING THE RESULTS
    actual_data=dataset.iloc[510:720, 2:6].values
    #Input data
    inputs=dataset.iloc[505:720, 2:6].values
    inputs=scaler.transform(inputs)
    #Creating a data structure with xx timesteps
    #Timesteps variations= 2,3,5 and 4 output
    testX=[]
    for i in range(5, 215):
        testX.append(inputs[i-5:i,0:4])
    testX=numpy.array(testX)
    #Reshape to a new dimension
    testX=numpy.reshape(testX,(testX.shape[0],testX.shape[1],4))
    #Identify the predicted values
    testPredict=model.predict(testX)
    #Invert predictions
    testPredict=scaler.inverse_transform(testPredict)
    #Calculate root mean squared error
    testScore=math.sqrt(mean_squared_error(actual_data,testPredict))
    print('Test Score (MAE)=', testScore)
    #Evaluating
    mape=numpy.abs((actual_data-testPredict)/actual_data).mean(axis=0)*100
    print(mape)
    # Create a xlsx
    import xlsxwriter
    workbook = xlsxwriter.Workbook('sub2/hasil prediktor.xlsx')
    worksheet = workbook.add_worksheet()
    row=0
    col=0
    for Latitude, Longitude, Heading, Kecepatan in (testPredict):
        worksheet.write(row,col, Latitude)
        worksheet.write(row,col+1, Longitude)
        worksheet.write(row,col+2, Heading)
        worksheet.write(row,col+3, Kecepatan)
        row += 1
    workbook.close()
    #Visualising the results/plot
    #Heading
    actual_data_heading = actual_data[0:210, 2:3]
    testPredict_heading = testPredict[0:210, 2:3]
    plt.plot(actual_data_heading, color='green', label='Data AIS (Heading)Aktual')
    plt.plot(testPredict_heading, color='blue', label='Data AIS (Heading) Hasil Prediksi')
    plt.title('Prediksi Data AIS (Heading) yang Hilang')
    plt.xlabel('Data Hilang ke-')
    plt.ylabel('Heading')
    plt.legend()
    plt.show()
    #Kecepatan
    actual_data_kecepatan = actual_data[0:210, 3:4]
    testPredict_kecepatan = testPredict[0:210, 3:4]
    plt.plot(actual_data_kecepatan, color='green', label='Data AIS (Kecepatan) Aktual')
    plt.plot(testPredict_kecepatan, color='blue', label='Data AIS (Kecepatan) Hasil Prediksi')
    plt.title('Prediksi Data AIS (Kecepatan) yang Hilang')
    plt.xlabel('Data Hilang ke-')
    plt.ylabel('Kecepatan(knots)')
    plt.legend()
    plt.show()

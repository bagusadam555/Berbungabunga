# Mengimpor library dan fungsi yang diperlukan
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
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import EarlyStopping
from keras.layers import LeakyReLU

def sistem_predictor_losses_data(namafile, trainingulang):
 
    # Memuat dataset
    dataset = pandas.read_csv(f'sub2/{namafile}')

    # Preprocessing data
    numpy.random.seed(1)
    random.seed(1)
    tf.random.set_seed(1)

    # Mengimpor data latih
    dataset_train = dataset.iloc[0:510, 2:6].values
    scaler = MinMaxScaler(feature_range=(0, 1))
    dataset_train_scaled = scaler.fit_transform(dataset_train)
    trainX, trainY = [], []
    for i in range(5, 510):
        trainX.append(dataset_train_scaled[i-5:i, 0:4])
        trainY.append(dataset_train_scaled[i, 0:4])
    trainX, trainY = numpy.array(trainX), numpy.array(trainY)
    trainX = numpy.reshape(trainX, (trainX.shape[0], trainX.shape[1], 4))
    val_size = int(len(trainX) * 0.2)
    valX = trainX[-val_size:]
    valY = trainY[-val_size:]
    trainX = trainX[:-val_size]
    trainY = trainY[:-val_size]
    
    # Membangun model RNN
    model = Sequential()
    model.add(LSTM(25, return_sequences=False, input_shape=(trainX.shape[1], 4)))
    model.add(Dropout(0.2))
    model.add(Dense(4))
    model.add(LeakyReLU(alpha=0.1))  # Menggunakan fungsi aktivasi Leaky ReLU

    # Mengompilasi model RNN
    opt = Adam(learning_rate=0.01)
    model.compile(loss='mean_absolute_error', optimizer=opt, metrics=['accuracy'])

    # Early stopping callback
    #callback = EarlyStopping(monitor='val_accuracy', patience=3, mode='max', baseline=0.9)

    # Melatih model RNN
    if trainingulang == False:
        history = model.fit(trainX, trainY, epochs=50, batch_size=2, validation_data=(valX, valY))
        model.save("adam.h5")
        print(f"Ini dia {history}")

        # Menampilkan grafik akurasi
        plt.plot(history.history['accuracy'])
        plt.plot(history.history['val_accuracy'])
        plt.title('Akurasi Model')
        plt.xlabel('Epoch')
        plt.ylabel('Akurasi')
        plt.legend(['Latih', 'Validasi'], loc='upper left')
        plt.show()

        # Menampilkan grafik loss
        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.title('Loss Model')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend(['Latih', 'Validasi'], loc='upper right')
        plt.show()
    else:
        model = load_model("adam.h5")
    
    # Melakukan prediksi dan validasi hasil
    actual_data = dataset.iloc[510:720, 2:6].values
    inputs = dataset.iloc[505:720, 2:6].values
    inputs = scaler.transform(inputs)
    testX = []
    for i in range(5, 215):
        testX.append(inputs[i-5:i, 0:4])
    testX = numpy.array(testX)
    testX = numpy.reshape(testX, (testX.shape[0], testX.shape[1], 4))
    testPredict = model.predict(testX)
    testPredict = scaler.inverse_transform(testPredict)
    testScore = math.sqrt(mean_squared_error(actual_data, testPredict))
    print('Skor Test (MAE) =', testScore)
    mape = numpy.abs((actual_data - testPredict) / actual_data).mean(axis=0) * 100
    print(mape)
    import xlsxwriter
    workbook = xlsxwriter.Workbook('sub2/hasil prediktor.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0
    for Latitude, Longitude, Heading, Kecepatan in (testPredict):
        worksheet.write(row, col, Latitude)
        worksheet.write(row, col+1, Longitude)
        worksheet.write(row, col+2, Heading)
        worksheet.write(row, col+3, Kecepatan)
        row += 1
    workbook.close()

    # Menampilkan hasil/plot
    actual_data_heading = actual_data[0:210, 2:3]
    testPredict_heading = testPredict[0:210, 2:3]
    plt.plot(actual_data_heading, color='green', label='Data AIS (Heading) Aktual')
    plt.plot(testPredict_heading, color='blue', label='Data AIS (Heading) Hasil Prediksi')
    plt.title('Prediksi Data AIS (Heading) yang Hilang')
    plt.xlabel('Data Hilang ke-')
    plt.ylabel('Heading')
    plt.legend()
    plt.show()

    actual_data_kecepatan = actual_data[0:210, 3:4]
    testPredict_kecepatan = testPredict[0:210, 3:4]
    plt.plot(actual_data_kecepatan, color='green', label='Data AIS (Kecepatan) Aktual')
    plt.plot(testPredict_kecepatan, color='blue', label='Data AIS (Kecepatan) Hasil Prediksi')
    plt.title('Prediksi Data AIS (Kecepatan) yang Hilang')
    plt.xlabel('Data Hilang ke-')
    plt.ylabel('Kecepatan (knots)')
    plt.legend()
    plt.show()

# Penggunaan fungsi untuk prediksi data
data = input("Masukkan nama Excel: ")
sistem_predictor_losses_data(data, False)

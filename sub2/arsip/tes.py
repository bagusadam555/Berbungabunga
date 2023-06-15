#Import library yang diperlukan
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

def sistem_predictor_losses_data(namafile, trainingulang):
 
    #Muat dataset
    dataset = pandas.read_csv(f'sub2/{namafile}')

    #PRAPEMROSESAN DATA
    #Set seed acak untuk reproduktibilitas

    numpy.random.seed(1)
    random.seed(1)
    tf.random.set_seed(1)

    #Impor set data latih
    dataset_train = dataset.iloc[0:510, 2:6].values
    #Normalisasi dataset
    scaler = MinMaxScaler(feature_range=(0, 1))
    dataset_train_scaled = scaler.fit_transform(dataset_train)
    #Konversi nilai-nilai menjadi matriks dataset
    trainX, trainY = [], []
    #Membuat xx timestep dari setiap nilai
    #Variasi timestep: 2, 3, 5
    for i in range(5, 510):
        #Berisi nilai berikutnya setelah xx timestep #Output = 4
        trainX.append(dataset_train_scaled[i-5:i, 0:4])
        #Digunakan untuk memprediksi nilai berikutnya (nilai masa depan)
        trainY.append(dataset_train_scaled[i, 0:4])
    #Konversi menjadi array numpy untuk dapat diterima dalam RNN
    trainX, trainY = numpy.array(trainX), numpy.array(trainY)
    #Reshape
    #Perlu mengubah array menjadi 3 dimensi untuk dapat diterima dalam RNN
    trainX = numpy.reshape(trainX, (trainX.shape[0], trainX.shape[1], 4))
    
    #MEMBANGUN RNN
    #Membuat dan melatih jaringan LSTM
    #Inisialisasi RNN
    model = Sequential()
    #Menambahkan lapisan input, lapisan LSTM pertama, dan Dropout regularisasi
    #Jumlah unit neuron LSTM: 1, 5, 10, 20, 25
    model.add(LSTM(25, return_sequences=False, input_shape=(trainX.shape[1], 4)))
    model.add(Dropout(0.2))
    #Menambahkan lapisan output
    model.add(Dense(4))
    #Mengompilasi RNN
    #Learning rate: 0.001, 0.005, 0.01, 0.1
    opt = Adam(learning_rate=0.01)
    model.compile(loss='mean_squared_error', optimizer=opt)
    #Melatih RNN dengan set data latih
    if trainingulang == False: #False untuk tidak melatih ulang
        model.fit(trainX, trainY, epochs=30, batch_size=2)
        model.save("adam.h5")
    else:
        from tensorflow.keras.models import load_model
        model = load_model("adam.h5")
    
    #MEMPREDIKSI DAN MEMVALIDASI HASIL
    actual_data = dataset.iloc[510:720, 2:6].values

    #Data masukan
    inputs = dataset.iloc[505:720, 2:6].values
    inputs = scaler.transform(inputs)
    #Membuat struktur data dengan xx timestep
    #Variasi timestep: 2, 3, 5 dan output 4
    testX = []
    for i in range(5, 215):
        testX.append(inputs[i-5:i, 0:4])
    testX = numpy.array(testX)
    #Reshape menjadi dimensi baru
    testX = numpy.reshape(testX, (testX.shape[0], testX.shape[1], 4))
    #Mengidentifikasi nilai-nilai yang diprediksi
    testPredict = model.predict(testX)
    #Inversi prediksi
    testPredict = scaler.inverse_transform(testPredict)
    #Menghitung akar mean squared error
    testScore = math.sqrt(mean_squared_error(actual_data, testPredict))
    print('Skor Uji (MSE) =', testScore)
    #Menghitung akurasi
    mape = numpy.abs((actual_data - testPredict) / actual_data).mean(axis=0) * 100
    print('Akurasi:', 100 - mape)
    
    #Membuat file Excel
    import xlsxwriter
    workbook = xlsxwriter.Workbook(f'sub2/hasil_prediktor_{namafile}.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0
    for Latitude, Longitude, Heading, Kecepatan in testPredict:
        worksheet.write(row, col, Latitude)
        worksheet.write(row, col+1, Longitude)
        worksheet.write(row, col+2, Heading)
        worksheet.write(row, col+3, Kecepatan)
        row += 1
    workbook.close()
    
    #Visualisasi hasil
    #Heading
    actual_data_heading = actual_data[0:210, 2:3]
    testPredict_heading = testPredict[0:210, 2:3]
    plt.plot(actual_data_heading, color='green', label='Data AIS (Heading) Aktual')
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
    plt.ylabel('Kecepatan (knots)')
    plt.legend()
    plt.show()

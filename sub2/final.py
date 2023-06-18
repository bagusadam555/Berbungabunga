# Mengimpor library dan semua fungsi
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

def sistem_predictor_losses_data(namafile, pilihan):
 
    # Memuat dataset
    dataset = pandas.read_csv(f'sub2/{namafile}')

    # PEMROSESAN DATA
    # Menetapkan randomseed untuk reproduktibilitas
    numpy.random.seed(1)
    random.seed(1)
    tf.random.set_seed(1)

    # Mengimpor set data latihan
    
    dataset_train = dataset.iloc[0:510, 2:6].values
    # Menormalkan dataset agar nilainya 0 sampai 1
    scaler = MinMaxScaler(feature_range=(0, 1))
    dataset_train_scaled = scaler.fit_transform(dataset_train)
    trainX, trainY = [], []
    # Membuat xx timestep setiap nilai
    
    for i in range(5, 510):
        # Berisi nilai berikutnya setelah xx timestep # Output: 4
        trainX.append(dataset_train_scaled[i-5:i, 0:4])
        # Digunakan untuk memprediksi nilai selanjutnya (nilai masa depan)
        trainY.append(dataset_train_scaled[i, 0:4])
    # Mengonversi menjadi array numpy agar dapat diterima dalam RNN
    trainX, trainY = numpy.array(trainX), numpy.array(trainY)
    # Reshape
    # Perlu mengubah array menjadi 3 dimensi agar dapat diterima dalam RNN
    trainX = numpy.reshape(trainX, (trainX.shape[0], trainX.shape[1], 4))
    # Membagi dataset menjadi set latihan dan validasi
    val_size = int(len(trainX) * 0.2)
    valX = trainX[-val_size:]
    valY = trainY[-val_size:]
    trainX = trainX[:-val_size]
    trainY = trainY[:-val_size]
    
    # Membangun RNN (variasi LSTM : 5, 9, 18)
    model = Sequential()
    model.add(LSTM(5, return_sequences=False, input_shape=(trainX.shape[1], 4)))
    model.add(Dropout(0.2))
    model.add(Dense(4))

    # Mengompilasi RNN (variasi learningrate : 0.001, 0.01, 0.1)
    opt = Adam(learning_rate=0.1)
    model.compile(loss='mean_absolute_error', optimizer=opt, metrics=['accuracy'])


    # Melatih RNN pada set data latihan
    import matplotlib.pyplot as plt
    if pilihan == False:
        history = model.fit(trainX, trainY, epochs=50, batch_size=1, validation_data=(valX, valY))#callbacks=[callback],
        model.save("adam.h5")
        print(f"Ini dia {history}")

        # Plot akurasi
        plt.plot(history.history['accuracy'])
        plt.plot(history.history['val_accuracy'])
        plt.title('Akurasi Model')
        plt.xlabel('Epoch')
        plt.ylabel('Akurasi')
        plt.legend(['Latihan', 'Validasi'], loc='upper left')
        plt.show()

        # Plot kerugian
        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.title('Kerugian Model')
        plt.xlabel('Epoch')
        plt.ylabel('Kerugian')
        plt.legend(['Latihan', 'Validasi'], loc='upper right')
        plt.show()
    else:
        model = load_model("adam.h5")
    
    # MEMPREDIKSI DAN MEMVALIDASI HASIL
    actual_data = dataset.iloc[510:720, 2:6].values
    # Data input
    inputs = dataset.iloc[505:720, 2:6].values
    inputs = scaler.transform(inputs)


    testX = []
    for i in range(5, 215):
        testX.append(inputs[i-5:i, 0:4])
    testX = numpy.array(testX)
    # Mengubah bentuk menjadi dimensi baru
    testX = numpy.reshape(testX, (testX.shape[0], testX.shape[1], 4))
    # Mengidentifikasi nilai yang diprediksi
    testPredict = model.predict(testX)
    # Memutar balik prediksi
    testPredict = scaler.inverse_transform(testPredict)
    # Menghitung RMSE
    testScore = math.sqrt(mean_squared_error(actual_data, testPredict))
    print('Skor Uji (RMSE) =', testScore)
    # Evaluasi
    mape = numpy.abs((actual_data - testPredict) / actual_data).mean(axis=0) * 100
    print(mape)
    # Membuat file xlsx
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

    # Visualisasi hasil/plot
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

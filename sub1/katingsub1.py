#Importing the libraries and all of the functions
import numpy
import pandas
from datetime import datetime
from google.colab import drive
drive.mount('/content/drive')
#Load the dataset and count losses data
#Kapal 1
FILE_NAME1 = pandas.read_csv('/content/drive/MyDrive/TA/Subsistem1 Skenario2 K1.csv')
kapal1 = FILE_NAME1.values
for i in range(len(kapal1)-1):
 timenow = datetime.strptime(kapal1[i][2],"%H:%M")
 timenext = datetime.strptime(kapal1[i+1][2], "%H:%M")
 difference = timenext - timenow
 if int(difference.total_seconds()) >= 7200:
    print('Ya, kapal 1 terjadi losses data AIS selama: ', int(difference.total_seconds()) , 'detik dan terindikasi melakukan IUU transshipment')
 elif int(180 < difference.total_seconds() < 7200):
    print('Ya, kapal 1 terjadi losses data AIS selama : ', int(difference.total_seconds()) , 'detik tetapi tidak terindikasi melakukan IUUtransshipment')
 else:
    print('Kapal 1 tidak terjadi losses data AIS dan tidak terindikasimelakukan IUU transshipment')
#Kapal 2
FILE_NAME2 = pandas.read_csv('/content/drive/MyDrive/TA/validasi fix subsistem1 k2.csv')
kapal2 = FILE_NAME2.values
for i in range(len(kapal2)-1):
 timenow = datetime.strptime(kapal2[i][2],"%H:%M:%S")
 timenext = datetime.strptime(kapal2[i+1][2], "%H:%M:%S")
 difference = timenext - timenow
 if int(difference.total_seconds()) >= 7200:
    print('Ya, kapal 2 terjadi losses data AIS selama: ', int(difference.total_seconds()) , 'detik dan terindikasi melakukan IUU transshipment')
 elif int(180 < difference.total_seconds() < 7200):
    print('Ya, kapal 2 terjadi losses data AIS selama : ', int(difference.total_seconds()) , 'detik tetapi tidak terindikasi melakukan IUUtransshipment')
 else:
    print('Kapal 2 tidak terjadi losses data AIS dan tidak terindikasimelakukan IUU transshipment')

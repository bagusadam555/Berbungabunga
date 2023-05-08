# Importing the libraries and all of the functions
import numpy
import pandas
from datetime import datetime

# Load the dataset and count losses data

# Kapal 1
FILE_NAME1 = pandas.read_csv('S1SK2K1.csv')
kapal1 = FILE_NAME1.values

for i in range(len(kapal1)-1):
    timenow = datetime.strptime(kapal1[i][2],"%H:%M")
    timenext = datetime.strptime(kapal1[i+1][2], "%H:%M")
    difference = timenext - timenow
    
    if int(difference.total_seconds()) >= 7200:
        print('Ya, kapal 1 terjadi losses data AIS selama: ', int(difference.total_seconds()), 'detik dan terindikasi melakukan IUU transshipment')
    elif int(180 < difference.total_seconds() < 7200):
        print('Ya, kapal 1 terjadi losses data AIS selama : ', int(difference.total_seconds()), 'detik tetapi tidak terindikasi melakukan IUU transshipment')
    else:
        print('Kapal 1 tidak terjadi losses data AIS dan tidak terindikasi melakukan IUU transshipment')


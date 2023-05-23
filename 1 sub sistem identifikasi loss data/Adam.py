# Importing the libraries and all of the functions
import numpy
import pandas
from datetime import datetime

# Load the dataset and count losses data
def sistem_identifikasi_losses_dataAIS(tipe_kapal,nama_file):
    # Kapal 
    isiexcel = pandas.read_csv(nama_file)
    kapal = isiexcel.values

    for i in range(len(kapal)-1):
        timenow = datetime.strptime(kapal[i][2],"%H:%M")
        timenext = datetime.strptime(kapal[i+1][2], "%H:%M")
        difference = timenext - timenow
        
        if int(difference.total_seconds()) >= 7200:
            print(f'Ya, kapal {tipe_kapal} terjadi losses data AIS selama: ', int(difference.total_seconds()), 'detik dan terindikasi melakukan IUU transshipment')
        elif int(180 < difference.total_seconds() < 7200):
            print(f'Ya, kapal {tipe_kapal} terjadi losses data AIS selama : ', int(difference.total_seconds()), 'detik tetapi tidak terindikasi melakukan IUU transshipment')
        else:
            print(f'Kapal {tipe_kapal} tidak terjadi losses data AIS dan tidak terindikasi melakukan IUU transshipment')

          

